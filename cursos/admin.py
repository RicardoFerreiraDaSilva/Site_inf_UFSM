from django.contrib import admin

from .models import Noticia

admin.site.register(Noticia)

from .models import Livro

admin.site.register(Livro)

from .models import GrupoPesquisa

@admin.register(GrupoPesquisa)
class GrupoPesquisaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lider')
    prepopulated_fields = {"slug": ("nome",)}  # gera slug automaticamente

from .models import Destaque

@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link')

from .models import ProjetoPET

admin.site.register(ProjetoPET)
