from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
    clinica = models.CharField(max_length=7)
    tipo = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now=True)
    data_lancamento = models.DateTimeField(verbose_name='Data do Lançamento')
    cpf = models.CharField(max_length=15)
    nome_paciente = models.CharField(max_length=70)
    celular_1 = models.CharField(max_length=15, blank=True, null=True)
    celular_2 = models.CharField(max_length=15, blank=True, null=True)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    ramal = models.CharField(max_length=4, blank=True, null=True)
    indicacao_midia = models.CharField(max_length=15, blank=True, null=True)
    nome_indicante = models.CharField(max_length=50, blank=True, null=True)
    cpf_indicante = models.CharField(max_length=15, blank=True, null=True)
    dentista_nick = models.CharField(max_length=25)
    especialidade = models.CharField(max_length=50)
    tabela = models.CharField(max_length=8)
    carteira_plano = models.CharField(max_length=12, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.clinica + ' ' + self.nome_paciente
