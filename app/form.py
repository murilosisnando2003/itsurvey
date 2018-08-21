from django import forms
from .models import Empresa
from django.utils.translation import gettext as _
from django import forms
from django.contrib.auth import authenticate

class AddForm(forms.ModelForm):
	class Meta:
		model= Empresa
		fields = ('name','email','cargo')
	escolher_empresa = forms.ModelChoiceField(Empresa.objects.all())	



class LoginForm(forms.Form):
   _user = None
   usuario = forms.CharField(
       label=_(u"Type your user")
   )
   senha = forms.CharField(
       label=_("Type you password"),
       max_length=20
   )

   def __init__(self,*args,**kwargs):
       super(LoginForm,self).__init__(*args,**kwargs)
       self.fields['usuario'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':_(u'informe um usuário válido')})
       self.fields['senha'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':_('informe a senha')})

   def clean(self):
       cleaned_data = self.cleaned_data
       if 'usuario' in cleaned_data and 'senha' in cleaned_data:
           self._user = authenticate(username=cleaned_data['usuario'], password=cleaned_data['senha'])
           if not self._user:
               self.add_error('usuario','Wrong user or password!')
       return cleaned_data

   @property
   def user(self):
       return self._user


