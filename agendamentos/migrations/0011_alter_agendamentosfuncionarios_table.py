# Generated by Django 3.2.8 on 2021-11-29 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0010_agendamentosfuncionarios'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='agendamentosfuncionarios',
            table='agendamento_funcionario',
        ),
    ]
