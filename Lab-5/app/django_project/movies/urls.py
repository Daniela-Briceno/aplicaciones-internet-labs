from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_generos, name="index"),
]
