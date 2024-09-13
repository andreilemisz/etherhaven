from django.shortcuts import render # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.http import HttpResponse # type: ignore

def paginalogin_inicial(request):
    return render(request, 'paginalogin/pagina_inicial.html')

def autenticacao(request):
    nome_usuario = request.POST["nome_usuario"]
    senha_usuario = request.POST["senha_usuario"]
    usuario = authenticate(username=nome_usuario, password=senha_usuario)
    
    if usuario is not None:
        login(request, usuario)
        # Redirect to a success page.
        return HttpResponse("Login efetuado com sucesso!")
        ...
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Login inválido")
        ...


# Create your views here.
