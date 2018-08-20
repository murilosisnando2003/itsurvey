from django.shortcuts import render
from .models import Empresa,Question,Cargo
from .form import AddForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
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
			return HttpResponse(reverse('', kwargs={'id':id}))

	data = {'form': form, 'id':id}
	# data['dados'] = Empresa.objects.all()
	return render (request,'app/home.html', data )


def questao(request):
	data = {}
	data['questoes'] = Question.objects.all()
	return render (request,'app/question.html', data)


def add_empresa (request):
	# data = {}
	# form = AddForm()
	empresas = Empresa.objects.all()
	return render(request,'app/form.html', {'empresas': empresas})

