from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial do app
    path('projetos/', views.projetos, name='projetos'),  # Lista de projetos
    path('projetos/cadastrar/', views.cadastrar_projeto, name='cadastrar_projeto'),  # Cadastro de projetos
    path('projetos/<int:projeto_id>/', views.projeto_detalhe, name='projeto_detalhe'),  # Detalhe de projeto por id
    path('login/', views.login_view, name='login'),
    # Apenas uma vez a URL logout, usando a view pronta do Django:
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('atividades/', views.atividades, name='atividades'),
    path('institucional/', views.institucional, name='institucional'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('estrutura/', views.estrutura, name='estrutura'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('base-demo/', views.base_demo, name='base_demo'),

]
