from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
