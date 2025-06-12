from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import (
    Projeto, Noticia, Livro, Atividade,
    GrupoPesquisa, Destaque, ProjetoPET
)
from .forms import (
    ProjetoForm, AtividadeForm, ProjetoPETForm
)

#Acesso rápido
def sistemas_informacao(request):
    return render(request, 'cursos/sistemas_informacao.html')

def ciencia_computacao(request):
    return render(request, 'cursos/ciencia_computacao.html')

# Página inicial com destaques e projetos PET
def home(request):
    destaques = Destaque.objects.all()
    petsi_destaques = ProjetoPET.objects.filter(grupo='SI')
    petcc_destaques = ProjetoPET.objects.filter(grupo='CC')
    return render(request, 'cursos/index.html', {
        'destaques': destaques,
        'petsi_destaques': petsi_destaques,
        'petcc_destaques': petcc_destaques,
    })

# Página de notícias
def noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'noticias.html', {'noticias': noticias})

def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'cursos/noticia_detail.html', {'noticia': noticia})

# Página de projetos
def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'cursos/projetos.html', {'projetos': projetos})

@login_required
def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'cursos/cadastrar_projeto.html', {'form': form})

def projeto_detalhe(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    return render(request, 'cursos/projeto_detalhe.html', {'projeto': projeto})

# Página de atividades
def atividades(request):
    atividades = Atividade.objects.all().order_by('-data')
    return render(request, 'cursos/atividades.html', {'atividades': atividades})

@login_required
def cadastrar_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('atividades')
    else:
        form = AtividadeForm()
    return render(request, 'cursos/cadastrar_atividade.html', {'form': form})

@login_required
def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('atividades')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'cursos/cadastrar_atividade.html', {'form': form})

@login_required
def excluir_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    atividade.delete()
    return redirect('atividades')

# Página de publicações
def publicacoes(request):
    publicacoes = Livro.objects.all()
    return render(request, 'cursos/publicacoes.html', {'publicacoes': publicacoes})

# Página de grupos de pesquisa
def pesquisa(request):
    grupos = GrupoPesquisa.objects.all()
    return render(request, 'cursos/pesquisa.html', {'grupos': grupos})

def grupo_detalhe(request, slug):
    grupo = get_object_or_404(GrupoPesquisa, slug=slug)
    return render(request, 'cursos/grupo_detalhe.html', {'grupo': grupo})

# Página de cadastro de projeto PET
@login_required
def cadastrar_projeto_pet(request):
    if request.method == 'POST':
        form = ProjetoPETForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjetoPETForm()
    return render(request, 'cursos/cadastrar_projeto_pet.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'cursos/login.html', {'form': form})

# Registro de usuário
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cursos/registrar.html', {'form': form})

# Páginas estáticas
def institucional(request):
    return render(request, 'cursos/institucional.html')

def estrutura(request):
    return render(request, 'cursos/estrutura.html')

def pessoas(request):
    return render(request, 'cursos/pessoas.html')

def base_demo(request):
    return render(request, 'cursos/base_demo.html')
