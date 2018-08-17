from django.contrib import admin
from .models import Empresa
from .models import Cargo
from .models import Question

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Cargo)
admin.site.register(Question)