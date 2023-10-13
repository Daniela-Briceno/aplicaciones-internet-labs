from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear_asignatura/', views.crear_asignatura, name="crear_asignatura"), 
]

"""
código de URL establece una ruta para la página principal (ruta raíz) de la aplicación, 
que está asociada a la vista index
"""