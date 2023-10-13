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

"""

def index(request):
    if request.method == 'POST':
        # Agregar nueva asignatura
        if 'agregar_asignatura' in request.POST:
            form = AsignaturaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        # Agregar nuevo alumno
        elif 'agregar_alumno' in request.POST:
            asignatura_id = int(request.POST.get('asignatura_id'))
            asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
            form = AlumnoForm(request.POST)
            if form.is_valid():
                alumno = form.save(commit=False)
                alumno.asignatura = asignatura
                alumno.save()
                return redirect('index')
    else:
        form_asignatura = AsignaturaForm()
        form_alumno = AlumnoForm()
    
    asignaturas = Asignatura.objects.all()
    
    return render(request, 'index.html', {
        'asignaturas': asignaturas,
        'form_asignatura': form_asignatura,
        'form_alumno': form_alumno
    })

def modificar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AsignaturaForm(instance=asignatura)
    
    return render(request, 'index.html', {
        'form_asignatura': form,
        'asignatura': asignatura,
        'form_alumno': AlumnoForm()
    })

def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    asignatura.delete()
    return redirect('index')
"""