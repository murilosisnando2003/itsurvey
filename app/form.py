from django import forms
from .models import Empresa

class AddForm(forms.ModelForm):
	class Meta:
		model= Empresa
		fields = ('name','email','cargo')
	escolher_empresa = forms.ModelChoiceField(Empresa.objects.all())	





