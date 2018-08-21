from django.shortcuts import render
from .models import Empresa,Question,Cargo
from .form import AddForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.forms import modelformset_factory
from django.core.mail import send_mail
from django.template.loader import get_template
from openpyxl.writer.excel import save_virtual_workbook, save_workbook
from openpyxl import Workbook
# Create your views here.


def escolher_empresa(request,id=None):
	instance = None
	if id:
		instance = get_object_or_404(Empresa, pk=id)

	form = AddForm(initial={'escolher_empresa':id},instance=instance)
	if request.POST:
		form = AddForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('question', kwargs={'id':id}))

	data = {'form': form, 'id':id}
	# data['dados'] = Empresa.objects.all()
	return render (request,'app/home.html', data )


def questao(request,id=None):
	message=None
	empresa = get_object_or_404(Empresa, pk=id)
	data = {}	
	class_formset_questao = modelformset_factory(Question,fields=['id','resposta'],extra=0)
	formset_questao = class_formset_questao(queryset=empresa.question_set.all())	
	if request.POST:
		formset_questao = class_formset_questao(request.POST,queryset=empresa.question_set.all())
		if formset_questao.is_valid():
			formset_questao.save()
			message=True
			template = get_template('app/email.html')
			email_html = template.render({'empresa':empresa})
			send_mail(
				'IT EDGE - Assessment',
				'cliente de email nao suporta html.',
				'info@edgeglobalsupply.com.br',
				['murilosisnando2003@hotmail.com'],
				fail_silently=False,
				html_message=email_html
				)
			if 'excel' in request.POST:
				return gera_excel(request,empresa)
	data['formset_questao'] = formset_questao #= question.objects.filter(empresa=id)
	data['message'] = message
	return render (request,'app/question.html', data)
	


def gera_excel(request, empresa):
	wb = Workbook(write_only=True)
	ws = wb.create_sheet()
	ws.append(['Empresa:', empresa.nome_empresa])
	ws.append(['pergunta','resposta'])
	for r in empresa.question_set.iterator():
		ws.append([r.questao, r.resposta])
	res = HttpResponse(save_virtual_workbook(wb),content_type='application/vnd.ms-excel')
	res['Content-Disposition'] = 'attachment; filename="{0}"'.format('teste.xlsx')
	return res
	



# def add_empresa (request):
# 	# data = {}
# 	# form = AddForm()
# 	empresas = Empresa.objects.all()
# 	return render(request,'app/form.html', {'empresas': empresas})

