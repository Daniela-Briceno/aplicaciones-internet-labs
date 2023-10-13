from django.contrib import admin
from .models import Asignatura, Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento')

admin.site.register(Asignatura)
admin.site.register(Alumno, AlumnoAdmin)

"""
Este código configura cómo se mostrarán y administrarán 
los modelos Asignatura y Alumno en el panel de administración de Django, 
proporcionando una visualización para el modelo Alumno
"""