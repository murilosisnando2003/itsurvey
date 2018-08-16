from django.contrib import admin
from .models import DadosEmpresa
from .models import Cargo
from .models import Question

# Register your models here.

admin.site.register(DadosEmpresa)
admin.site.register(Cargo)
admin.site.register(Question)