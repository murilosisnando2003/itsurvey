from django.shortcuts import render
from .models import Empresa,Question,Cargo
from .form import AddForm
# Create your views here.


def consulta_dados(request):
	data = {}
	data['dados'] = Empresa.objects.all()
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

