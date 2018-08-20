from django.urls import path
from . import views



urlpatterns = [
path('escolher-empresa', views.escolher_empresa,name='escolherempresa'),
path('escolher-empresa/<int:id>', views.escolher_empresa,name='escolherempresapk'),
path('questao/<int:id>',views.questao,name='question')

]