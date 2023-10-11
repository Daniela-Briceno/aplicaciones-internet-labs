from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_asignaturas, name='lista_asignaturas'),
    path('asignatura/<int:asignatura_id>/agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    # Añade otras URLs para modificar o eliminar asignaturas y alumnos
]
