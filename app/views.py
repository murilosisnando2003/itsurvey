from django.shortcuts import render
from .models import DadosEmpresa
from .form import AddForm
# Create your views here.


def consulta_dados(request):
	data = {}
	data['dados'] = DadosEmpresa.objects.all()
	return render (request,'app/home.html', data )


def questao(request):
	data = {}
	data['questoes'] = Question.objects.all()
	return render (request,'app/question.html', data)


def add_empresa (request):
	data = {}
	form = AddForm()
	data['form'] = form
	return render(request,'app/form.html',data)

