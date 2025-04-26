from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'voto')  # Exibe essas colunas na listagem
    search_fields = ('nome', 'voto')          # Adiciona barra de busca por nome e voto
    list_filter = ('voto',) 

# Registre o modelo junto com a classe de configuração
admin.site.register(Usuario, UsuarioAdmin)
