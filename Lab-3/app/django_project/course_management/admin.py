from django.contrib import admin
from .models import Asignatura, Alumno, AsignaturaAlumno

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    search_fields = ('nombre', 'codigo')

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno')

class AsignaturaAlumnoAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'alumno')
    search_fields = ('asignatura__nombre', 'alumno__nombre')

admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(AsignaturaAlumno, AsignaturaAlumnoAdmin)
