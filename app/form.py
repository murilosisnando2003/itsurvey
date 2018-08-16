from django.forms import ModelForm
from .models import DadosEmpresa

class AddForm(ModelForm):
	class meta:
		model= DadosEmpresa
		fields = ['nome_empresa','name','email','cargo']