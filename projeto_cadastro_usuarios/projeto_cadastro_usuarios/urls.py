
from django.contrib import admin
from django.urls import path
#importando o views de dentro do meu app
from app_cad_users import views

urlpatterns = [
    #ROTA, VIEWS RESPONSÁVEL(função responsável),NOME DE REFERÊNCIA
    #facebook.com #vazio é o link inicial
    path('', views.home, name='home'),
    #facebook.com/usuarios
   path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
