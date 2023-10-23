from django import forms
from .models import Curso, Alumno

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo']  # Los campos que deseas incluir en el formulario

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'cursos']  # Los campos que deseas incluir en el formulario
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

        
