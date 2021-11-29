from django.db import models
from .help import validate_CPF

class Funcionario(models.Model):
    class Meta:
        db_table = 'funcionario'
    
    #cpf = models.CharField(unique=True, max_length=14, validators=[validate_CPF])
    cpf = models.CharField(unique=True, max_length=14)
    nome = models.CharField(max_length = 200)
    email = models.EmailField()
    senha = models.CharField(max_length = 64)
    linha = models.IntegerField(null=True)
    ponto = models.IntegerField(null=True)
    tipo = models.CharField(max_length = 10, null=True)

    def __str__(self) -> str:
        return self.cpf