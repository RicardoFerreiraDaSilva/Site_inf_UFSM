from django.shortcuts import render, redirect
from .forms import ProjetoForm
from django.shortcuts import render, get_object_or_404
from .models import Projeto

def projeto_detalhe(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    return render(request, 'cursos/projeto_detalhe.html', {'projeto': projeto})
def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projetos')  # redireciona para a lista de projetos
    else:
        form = ProjetoForm()
    return render(request, 'cursos/cadastrar_projeto.html', {'form': form})

def index(request):
    return render(request, 'cursos/index.html')

def projetos(request):
    projetos = Projeto.objects.all()  # busca todos os projetos no banco
    return render(request, 'cursos/projetos.html', {'projetos': projetos})

def atividades(request):
    return render(request, 'cursos/atividades.html')

def institucional(request):
    return render(request, 'cursos/institucional.html')

def pesquisa(request):
    return render(request, 'cursos/pesquisa.html')

def publicacoes(request):
    return render(request, 'cursos/publicacoes.html')

def estrutura(request):
    return render(request, 'cursos/estrutura.html')

def pessoas(request):
    return render(request, 'cursos/pessoas.html')
    