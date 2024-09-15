from django.db import models # type: ignore
from django.contrib.auth.models import User

class Tarefa(models.Model):
    nome_tarefa = models.CharField(max_length=100)
    status_tarefa = models.BooleanField(default=False)
    descricao_tarefa = models.TextField(blank=True)
    usuariovinculado = models.ForeignKey(User, on_delete=models.CASCADE)
    # data_vencimento = ?                               -> Como fazer?
    # lembrete_tarefa = ?                               -> Como fazer?
    # prioridade_tarefa = models.BooleanField(default=False) -> implementar futuramente
    
    def __str__(self) -> str:
        return f"{self.nome_tarefa}"
    
# Create your models here.
