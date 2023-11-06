from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone, Interesse

# Register your models here.

#Classe para exibir Telefones no cad. de Contato
class Telefones(admin.TabularInline):
    model = Telefone
    extra = 1

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_display_links = ['id', 'nome']
    list_filter = ['data_nascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]
    filter_horizontal = ['interesses']

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)