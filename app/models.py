from django.db import models
from django.utils.timezone import now

# Create your models here.

class Cargo(models.Model):
	nome_cargo = models.CharField(max_length=100)
	def __str__ (self):
		return self.nome_cargo


class Empresa (models.Model):
	nome_empresa = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=70)
	cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
	def __str__(self):
		return self.nome_empresa



class Question(models.Model):
	# empresa = models.OneToOneField(
    # Empresa,
    # on_delete=models.CASCADE,
    # verbose_name="related empresa",)
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	questao = models.CharField(max_length= 500)
	resposta = models.TextField()
	data_resposta = models.DateField(default=now, blank=True)
	def __str__(self):
		return self.questao

# class Answer(models.Model):
# 	question = models.ForeignKey(Question,on_delete=models.CASCADE)
# 	empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
# 	resposta = models.TextField()
# 	data_resposta = models.DateField(default=now, blank=True)
# 	def __str__(self):
# 		return self.resposta		












