from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjetoForm
from .models import Projeto, Noticia, Livro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'cursos/publicacoes.html', {'livros': livros})

def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'cursos/noticia_detail.html', {'noticia': noticia})

def pagina_inicial(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')[:5] 
    return render(request, 'nome_da_template.html', {'noticias': noticias})

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

def index(request):
    return render(request, 'cursos/index.html')

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'cursos/projetos.html', {'projetos': projetos})

def atividades(request):
    return render(request, 'cursos/atividades.html')

def institucional(request):
    return render(request, 'cursos/institucional.html')

def pesquisa(request):
    return render(request, 'cursos/pesquisa.html')

def estrutura(request):
    return render(request, 'cursos/estrutura.html')

def pessoas(request):
    return render(request, 'cursos/pessoas.html')

def base_demo(request):
    return render(request, 'cursos/base_demo.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cursos/registrar.html', {'form': form})
