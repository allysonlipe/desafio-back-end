from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('selecionar-tudo', views.selecionar_tudo),
    path('selecionar-pessoa/<str:id>', views.selecionar_pessoa),
    path('inserir-pessoa', views.inserir_pessoa),
    path('atualizar-pessoa', views.atualizar_pessoa),
    path('deletar-pessoa/<str:id>', views.deletar_pessoa),
]
