from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
        return self.titulo
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100, blank=True)
    ano_publicacao = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, blank=True)
    descricao = models.TextField(blank=True)
    arquivo_pdf = models.FileField(upload_to='livros/', blank=True, null=True)
    capa = models.ImageField(upload_to='capas_livros/', blank=True, null=True)

    def __str__(self):
        return self.titulo
