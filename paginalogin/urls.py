from django.urls import path # type: ignore
from paginalogin.views import paginalogin_inicial, autenticacao

app_name = "paginalogin"

urlpatterns = [
    path("", paginalogin_inicial, name="paginalogin_inicial"),
    # path('<int:contact_id>/', contact_log_views.contact, name='contact'), -> Transformar em TarefaID
    # path("search/", contact_log_views.contact_log_search, name="search"), -> Para página de Search
                                                # Precisa de uma URL separada para search ou só filtro?
    # path("", NOME-CLASSE.as_view()),
    # path("", views.lista_todo_visualizacao, name="lista_todo_visualizacao"),
    ]