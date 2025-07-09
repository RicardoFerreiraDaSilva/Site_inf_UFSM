from django.db import models
from django.utils import timezone  # ✅ IMPORTADO NO TOPO
from django.utils.text import slugify

# MODELO: Projeto
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    link = models.URLField(
        max_length=200, 
        blank=True, 
        null=True, 
        help_text="Link para o repositório ou site do projeto (opcional)."
    )
    imagem = models.ImageField(
        upload_to='projetos_alunos/', 
        blank=True, 
        null=True, 
        help_text="Imagem de destaque do projeto (opcional)."
    )

    def __str__(self):
        return self.titulo

# ✅ MODELO 'Noticia' UNIFICADO E CORRIGIDO
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(
        max_length=255, 
        help_text="Um resumo curto da notícia para a página inicial."
    )
    conteudo = models.TextField(null=True, blank=True)
    data = models.DateTimeField(default=timezone.now) 
    imagem = models.ImageField(
        upload_to='noticias/', 
        null=True, 
        blank=True,
        help_text="Imagem de destaque da notícia (opcional)."
    )
    
    def __str__(self):
        return self.titulo

# MODELO: Livro
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano = models.IntegerField()
    descricao = models.TextField()
    capa = models.ImageField(upload_to='capas_livros/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

# MODELO: Atividade
class Atividade(models.Model):
    TIPO_CHOICES = [
        ('Palestra', 'Palestra'),
        ('Workshop', 'Workshop'),
        ('Feira', 'Feira'),
        ('Outra', 'Outra'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data = models.DateField()
    local = models.CharField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='atividades/', blank=True, null=True)

    def __str__(self):
        return self.titulo

# MODELO: Grupo de Pesquisa
class GrupoPesquisa(models.Model):
    nome = models.CharField(max_length=200)
    lider = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

# MODELO: Destaque
class Destaque(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='destaques/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

# MODELO: Projeto PET
class ProjetoPET(models.Model):
    GRUPO_CHOICES = [
        ('SI', 'Sistemas de Informação'),
        ('CC', 'Ciência da Computação'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    grupo = models.CharField(max_length=2, choices=GRUPO_CHOICES)
    ordem = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='projetos_pet/', blank=True, null=True)
    pet_tipo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_grupo_display()})"
 
# MODELO: Publicacao
class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    link = models.URLField()
    ano = models.IntegerField()
    resumo = models.TextField(
        null=True, 
        blank=True, 
        help_text="Uma breve descrição ou resumo do artigo."
    )

    def __str__(self):
        return self.titulo

# MODELO: Evento
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao_curta = models.CharField(max_length=255, help_text="Aparece no card do carrossel na página inicial.")
    imagem = models.ImageField(upload_to='eventos_imagens/')
    conteudo_completo = models.TextField()
    data_evento = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo