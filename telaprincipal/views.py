from django.shortcuts import render # type: ignore
from gestortarefas.models import Tarefa


def telamestre(request):
    tarefas = Tarefa.objects.filter(usuariovinculado=request.user)
    return render(request, 'telaprincipal/telamestre.html', {'tarefas': tarefas})



# Create your views here.
