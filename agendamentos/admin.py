from django.contrib import admin
from django.contrib.admin.decorators import display, register
from .models import Agendamento

@admin.register(Agendamento)
class UsuarioAdmin(admin.ModelAdmin):
    
    list_display = ('funcionario_cpf', 'data', 'reserva')