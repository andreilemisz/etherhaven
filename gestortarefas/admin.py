from django.contrib import admin
from gestortarefas import models

@admin.register(models.Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = "nome_tarefa", "status_tarefa", "usuariovinculado",
    search_fields = "nome_tarefa", "descricao_tarefa", "usuariovinculado",
    list_per_page = 20
    list_max_show_all = 50

# Register your models here.