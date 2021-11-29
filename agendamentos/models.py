from django.core.files.utils import FileProxyMixin
from django.db import models
from django.db.models.expressions import Func
from usuarios.models import Funcionario
class Agendamento(models.Model):
    class Meta:
        db_table = 'agendamento'
        unique_together = (('funcionario_cpf', 'data'),)

    funcionario_cpf = models.ForeignKey(Funcionario, on_delete = models.DO_NOTHING)
    data = models.DateField()
    reserva = models.BooleanField()

    def __str__(self):
        return "%s %s" % (self.funcionario_cpf, self.data)
 
class AgendamentosFuncionarios(models.Model):
    pass