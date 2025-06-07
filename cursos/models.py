from django.db import models
from django.utils.text import slugify

# MODELO: Projeto
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo


# MODELO: Notícia
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)

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


# MODELO: Projeto PET (substitui PetDestaque)
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
