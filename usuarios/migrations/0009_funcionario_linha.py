# Generated by Django 3.2.8 on 2021-11-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_funcionario_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='linha',
            field=models.IntegerField(null=True),
        ),
    ]
