from django.contrib import admin
from paciente.models import Paciente

# Register your models here.

class PacienteLista(admin.ModelAdmin):
    list_display = ('clinica', 'nome_paciente', 'data_cadastro')
    list_filter = ('clinica',)

admin.site.register(Paciente, PacienteLista)

