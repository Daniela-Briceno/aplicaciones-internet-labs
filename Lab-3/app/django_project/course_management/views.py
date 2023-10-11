from django.shortcuts import render, get_object_or_404, redirect
from course_management.models import Asignatura, Alumno

def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def agregar_alumno(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)

    if request.method == 'POST':
        # Procesar el formulario de agregar alumno
        # Aquí debes crear un formulario de Django para agregar un alumno a la asignatura

    return render(request, 'agregar_alumno.html', {'asignatura': asignatura})

# Otras vistas para modificar o eliminar asignaturas y alumnos
