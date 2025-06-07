from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='index'),  # aqui: views.home no lugar de views.index
    
    # Páginas principais
    path('institucional/', views.institucional, name='institucional'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('estrutura/', views.estrutura, name='estrutura'),
    path('pessoas/', views.pessoas, name='pessoas'),

    # Projetos
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<int:projeto_id>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('cadastrar_projeto/', views.cadastrar_projeto, name='cadastrar_projeto'),

    # Autenticação
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar_usuario, name='registrar'),

    # Publicações
    path('publicacoes/', views.publicacoes, name='publicacoes'),

    # Notícias
    path('noticias/', views.noticias, name='noticias'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),

    # Atividades
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/cadastrar/', views.cadastrar_atividade, name='cadastrar_atividade'),
    path('atividades/gerenciar/', views.listar_atividades, name='listar_atividades'),
    path('atividades/editar/<int:id>/', views.editar_atividade, name='editar_atividade'),
    path('atividades/excluir/<int:id>/', views.excluir_atividade, name='excluir_atividade'),

    # Projeto PET
    path('cadastrar-projeto-pet/', views.cadastrar_projeto_pet, name='cadastrar_projeto_pet'),

    # Grupos de pesquisa
    path('grupos/<slug:slug>/', views.grupo_detalhe, name='grupo_detalhe'),
]
