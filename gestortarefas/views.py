from django.shortcuts import render
from gestortarefas.models import Tarefa

def gestortarefas_paginateste(request):
    
    # tarefas = Tarefa.objects.all().order_by("prioridade_tarefa")
    # context_object_name = "conjunto_tarefas"
    
    return render(request, 'gestortarefas/base.html')

def gestortarefas_paginamobile(request):
    
    # tarefas = Tarefa.objects.all().order_by("prioridade_tarefa")
    # context_object_name = "conjunto_tarefas"
    
    return render(request, 'gestortarefas/mobile.html')

def gestortarefas_paginainicial(request):
    
    # tarefas = Tarefa.objects.all().order_by("prioridade_tarefa")
    # context_object_name = "conjunto_tarefas"
    
    return render(request, 'gestortarefas/paginainicial.html')
# Create your views here.
