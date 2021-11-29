#from django.contrib import admin
#from .models import Usuario

#admin.site.register(Usuario)
from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Funcionario

@admin.register(Funcionario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'email', 'senha', 'linha', 'ponto', 'tipo')
    search_fields = ('cpf', 'nome', 'email', 'linha','ponto', 'tipo')
    readonly_fields = ('senha',)