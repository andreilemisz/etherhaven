from django.urls import path # type: ignore
from paginalogin.views import paginalogin_inicial

app_name = "paginalogin"

urlpatterns = [
    path("", paginalogin_inicial, name="paginalogin_inicial"),
    ]