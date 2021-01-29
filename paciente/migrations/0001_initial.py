# Generated by Django 3.1.5 on 2021-01-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinica', models.CharField(max_length=7)),
                ('tipo', models.CharField(max_length=15)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('data_lancamento', models.DateTimeField()),
                ('cpf', models.CharField(max_length=15)),
                ('nome_paciente', models.CharField(max_length=70)),
                ('celular_1', models.CharField(max_length=15)),
                ('celular_2', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=13)),
                ('ramal', models.CharField(max_length=4)),
                ('indicacao_midia', models.CharField(max_length=15)),
                ('nome_indicante', models.CharField(max_length=50)),
                ('cpf_indicante', models.CharField(max_length=15)),
                ('dentista_nick', models.CharField(max_length=25)),
                ('especialidade', models.CharField(max_length=50)),
                ('tabela', models.CharField(max_length=8)),
                ('carteira_plano', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
    ]
