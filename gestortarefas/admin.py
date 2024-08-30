from django.contrib import admin
from gestortarefas import models

@admin.register(models.Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = "nome_tarefa", "prioridade_tarefa", "status_tarefa"
    ordering = "prioridade_tarefa",
    search_fields = "nome_tarefa", "descricao_tarefa",
    list_per_page = 20
    list_max_show_all = 50

# Register your models here.