from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjetoForm
from .models import Projeto, Noticia, Livro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Projeto, Noticia, Livro, Atividade, GrupoPesquisa
from .forms import ProjetoForm, AtividadeForm


# Página inicial
def index(request):
    return render(request, 'cursos/index.html')


# Notícias
def noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'noticias.html', {'noticias': noticias})



def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'cursos/noticia_detail.html', {'noticia': noticia})


# Página inicial com notícias recentes
def pagina_inicial(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')[:5]
    return render(request, 'nome_da_template.html', {'noticias': noticias})


# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
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


# Projetos
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

# Atividades
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

from django.shortcuts import render, redirect
from .forms import AtividadeForm

def cadastrar_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('atividades')  # redireciona para a lista de atividades
    else:
        form = AtividadeForm()
    
    return render(request, 'cursos/cadastrar_atividade.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Atividade
from .forms import AtividadeForm

def listar_atividades(request):
    atividades = Atividade.objects.all().order_by('-data')
    return render(request, 'cursos/listar_atividades.html', {'atividades': atividades})

def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('listar_atividades')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'cursos/cadastrar_atividade.html', {'form': form})

def excluir_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    atividade.delete()
    return redirect('listar_atividades')

# Publicações (Livros)

def publicacoes(request):
    publicacoes = Livro.objects.all()
    return render(request, 'cursos/publicacoes.html', {'publicacoes': publicacoes})

# Grupos de Pesquisa

from .models import GrupoPesquisa  


def pesquisa(request):
    grupos = GrupoPesquisa.objects.all()
    return render(request, 'cursos/pesquisa.html', {'grupos': grupos})

def grupo_detalhe(request, slug):
    grupo = get_object_or_404(GrupoPesquisa, slug=slug)
    return render(request, 'cursos/grupo_detalhe.html', {'grupo': grupo})


# Páginas estáticas
def institucional(request):
    return render(request, 'cursos/institucional.html')

def estrutura(request):
    return render(request, 'cursos/estrutura.html')

def pessoas(request):
    return render(request, 'cursos/pessoas.html')

def base_demo(request):
    return render(request, 'cursos/base_demo.html')
