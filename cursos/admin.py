from django.contrib import admin
# Importando todos os models de uma vez para organizar
from .models import (
    Noticia,
    Livro,
    GrupoPesquisa,
    Destaque,
    ProjetoPET,
    Publicacao,
    Evento  # ✅ Model Evento importado
)

# Registros simples
admin.site.register(Noticia)
admin.site.register(Livro)
admin.site.register(ProjetoPET)
admin.site.register(Publicacao)


# Registros com classes personalizadas
@admin.register(GrupoPesquisa)
class GrupoPesquisaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lider')
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link')


# ✅ Novo registro para Evento
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """
    Personaliza a exibição de Eventos no painel de admin.
    """
    list_display = ('titulo', 'data_evento', 'data_publicacao')
    list_filter = ('data_evento',) # Adiciona um filtro por data na lateral
    search_fields = ('titulo', 'descricao_curta') # Adiciona uma barra de busca