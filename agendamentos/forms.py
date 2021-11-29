from django import forms
from agendamentos.models import Agendamento

# creating a form
class AgendamentosForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Agendamento
 
        # specify fields to be used
        fields = [
            "id",
            "funcionario_cpf",
            "data",
            "reserva",
        ]