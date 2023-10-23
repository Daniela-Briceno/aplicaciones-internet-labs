from django.shortcuts import get_object_or_404, redirect, render
from .models import Curso, Alumno
from .forms import CursoForm, AlumnoForm

def index(request):
    # Obtengo alumnos y cursos
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()

    # Manejar el formulario del curso
    if request.method == 'POST' and 'submit_curso' in request.POST:
        formCurso = CursoForm(request.POST)
        if formCurso.is_valid():
            formCurso.save()
            # Redirigir a la misma página después de guardar el curso
            return redirect('index')
    else:
        formCurso = CursoForm()

    # Manejar el formulario del alumno
    if request.method == 'POST' and 'submit_alumno' in request.POST:
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            # Redirigir a la misma página después de guardar el alumno
            return redirect('index')
    else:
        formAlumno = AlumnoForm()

    return render(request, 'index.html', {'formCurso': formCurso, 'formAlumno': formAlumno, 'alumnos': alumnos, 'cursos': cursos})

def modificar_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    # Lógica para modificar el curso
    return render(request, 'index.html', {'curso': curso})

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    # Lógica para eliminar el curso
    curso.delete()
    return redirect('index')  # Redirige a la página de lista de cursos después de eliminar

def modificar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    # Lógica para modificar el alumno
    return render(request, 'index.html', {'alumno': alumno})

def eliminar_alumno(request, alumno_id):
    # Obtiene el objeto del alumno basado en su id
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    
    # Obtiene los cursos asociados al alumno antes de eliminarlo
    cursos_asociados = alumno.cursos.all()  # Obtiene todos los cursos asociados al alumno
    
    # Lógica para eliminar el alumno
    alumno.delete()
    
    # Elimina el alumno de todos los cursos asociados
    for curso in cursos_asociados:
        curso.alumnos.remove(alumno)
    
    return redirect('index')

def agregar_curso(request):
    cursos = Curso.objects.all()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'index.html', {'form': form, 'cursos': cursos})
	
def agregar_alumno(request):
    alumnos = Alumno.objects.all()
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'index.html', {'form': form, 'alumnos': alumnos})