from django.contrib import admin

from .models import Noticia

admin.site.register(Noticia)

from .models import Livro

admin.site.register(Livro)
