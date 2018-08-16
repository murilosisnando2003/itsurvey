from django.db import models

# Create your models here.

class Cargo(models.Model):
	nome_cargo = models.CharField(max_length=100)
	def __str__ (self):
		return self.nome_cargo


class DadosEmpresa (models.Model):
	nome_empresa = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=70)
	cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
	def __str__(self):
		return self.name



class Question(models.Model):
	questao = models.CharField(max_length= 500)
	resposta = models.TextField()
	def __str__(self):
		return self.questao







