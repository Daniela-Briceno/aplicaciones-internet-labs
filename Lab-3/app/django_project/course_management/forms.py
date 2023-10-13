from django import forms
from .models import Asignatura, Alumno

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'codigo']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']

"""
Formularios para a crear instancias de Asignatura y Alumno 
utilizando el formulario HTML correspondiente y
 manejarán la validación y el procesamiento de datos para estos modelos. 
 Por ejemplo, al crear un nuevo Alumno, 
 puedes utilizar AlumnoForm para proporcionar una interfaz de usuario y 
 validar los datos antes de guardarlo en la base de datos.
"""