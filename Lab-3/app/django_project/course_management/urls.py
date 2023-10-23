from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('curso/modificar/<int:curso_id>/', views.modificar_curso, name='modificar_curso'),
    path('curso/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),

    path('cursos/agregar/', views.agregar_curso, name='agregar_curso'),

    path('alumno/modificar/<int:alumno_id>/', views.modificar_alumno, name='modificar_alumno'),
    path('alumno/eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),

]