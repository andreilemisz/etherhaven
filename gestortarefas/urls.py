from django.urls import path
from . import views

app_name = "gestortarefas"

urlpatterns = [
    # path('<int:contact_id>/', contact_log_views.contact, name='contact'), -> Transformar em TarefaID
    # path("search/", contact_log_views.contact_log_search, name="search"), -> Para página de Search
                                                # Precisa de uma URL separada para search ou só filtro?
    path("teste/", views.gestortarefas_paginateste, name="gestortarefas_paginateste"),
    path("mobile/", views.gestortarefas_paginamobile, name="gestortarefas_paginamobile"),
    path("", views.gestortarefas_paginainicial, name="gestortarefas_paginainicial"),
    ]