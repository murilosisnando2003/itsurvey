from django.shortcuts import render
from .models import DadosEmpresa
# Create your views here.


def consulta_dados(request):
	data = {}
	data['dados'] = DadosEmpresa.objects.all()
	return render (request,'app/home.html', data )


def questao(request):
	data = {}
	data['questoes'] = Question.objects.all()
	return render (request,'app/question.html', data)