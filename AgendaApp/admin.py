from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone

# Register your models here.

#Classe para exibir Telefones no cad. de Contato
class Telefones(admin.StackedInline):
    model = Telefone

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_filter = ['data_nascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)