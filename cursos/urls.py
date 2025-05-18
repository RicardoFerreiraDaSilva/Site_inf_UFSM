from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projetos/', views.projetos, name='projetos'),
    path('atividades/', views.atividades, name='atividades'),
    path('institucional/', views.institucional, name='institucional'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('estrutura/', views.estrutura, name='estrutura'),
    path('pessoas/', views.pessoas, name='pessoas'),
]
