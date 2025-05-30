from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('atividades/', views.atividades, name='atividades'),
    path('institucional/', views.institucional, name='institucional'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('publicacoes/', views.lista_livros, name='publicacoes'),
    path('estrutura/', views.estrutura, name='estrutura'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<int:projeto_id>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('cadastrar_projeto/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),
]
