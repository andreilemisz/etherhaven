from django.urls import path # type: ignore
from gestortarefas.views import lista_todo_visualizacao

app_name = "gestortarefas"

#urlpatterns = [
        # path('<int:contact_id>/', contact_log_views.contact, name='contact'), -> Transformar em TarefaID
        # path("search/", contact_log_views.contact_log_search, name="search"), -> Para página de Search
                                                # Precisa de uma URL separada para search ou só filtro?
#path("", lista_todo_visualizacao.as_view()),
        # path("", views.lista_todo_visualizacao, name="lista_todo_visualizacao"),
#    ]