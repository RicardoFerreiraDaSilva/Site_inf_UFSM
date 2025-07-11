from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

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

    # Publicações Acadêmicas
   # Garanta que a rota para a LISTA de publicações existe
    path('publicacoes-academicas/', views.publicacoes_academicas, name='publicacoes_academicas'),

    # ✅ ESTA É A LINHA QUE PRECISA ESTAR CORRETA ✅
    # A URL deve ser no plural: 'publicacoes/'
    path('publicacoes/<int:pk>/', views.publicacao_detail, name='publicacao_detail'),

    # Notícias
    path('noticias/', views.noticias, name='noticias'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),

    # Atividades
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/cadastrar/', views.cadastrar_atividade, name='cadastrar_atividade'),
    path('atividades/gerenciar/', views.editar_atividade, name='gerenciar_atividades'),
    path('atividades/editar/<int:id>/', views.editar_atividade, name='editar_atividade'),
    path('atividades/excluir/<int:id>/', views.excluir_atividade, name='excluir_atividade'),

    # Projetos PET
    path('cadastrar-projeto-pet/', views.cadastrar_projeto_pet, name='cadastrar_projeto_pet'),

    # Grupos de pesquisa
    path('grupos/<slug:slug>/', views.grupo_detalhe, name='grupo_detalhe'),

    #Acesso rápido
    path('sistemas_informacao/', views.sistemas_informacao, name='sistemas_informacao'),
    path('ciencia_computacao/', views.ciencia_computacao, name='ciencia_computacao'),
    path('pos-graduacao-cc/', views.pos_graduacao_cc, name='pos_graduacao_cc'),
    path('duvidas/', views.duvidas, name='duvidas'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('moodle/', views.moodle_guia, name='moodle_guia'),
    
    #Novo destaque
    path('eventos/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),

]
