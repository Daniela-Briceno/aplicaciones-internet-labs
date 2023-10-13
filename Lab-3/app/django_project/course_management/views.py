from django.shortcuts import render, get_object_or_404, redirect
from .models import Asignatura, Alumno
from .forms import AsignaturaForm, AlumnoForm

def index(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'index.html',{'Asignaturas':asignaturas})

def crear_asignatura(request):
    context = {
        'form': AsignaturaForm()
    }
    return render(request, 'index.html', context)
