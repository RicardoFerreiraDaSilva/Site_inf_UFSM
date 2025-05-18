from django.shortcuts import render

def index(request):
    return render(request, 'cursos/index.html')

def projetos(request):
    return render(request, 'cursos/projetos.html')

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
    