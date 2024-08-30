from django.shortcuts import render
from django.views.generic import ListView
from gestortarefas.models import Tarefa


class lista_todo_visualizacao(ListView):
    model = Tarefa
    template_name = "gestortarefas/paginainicial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context    

""" 
Versão antiga com request
def gestortarefas_paginainicial(request):
    
    tarefas = Tarefa.objects.all().order_by("prioridade_tarefa")
    context_object_name = "conjunto_tarefas"
    
    return render(request, 'gestortarefas/paginainicial.html')
    """
# Create your views here.
