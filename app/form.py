from django import forms
from .models import Empresa

class AddForm(forms.ModelForm):
	class meta:
		model= Empresa
		fields = ('nome_empresa','name','email','cargo')



