from django.test import TestCase
from django.urls import reverse
from .models import Asignatura, Alumno
from .forms import AsignaturaForm, AlumnoForm

class AsignaturaModelTests(TestCase):

    def test_asignatura_creation(self):
        asignatura = Asignatura.objects.create(nombre="Matemáticas", codigo="MAT101")
        self.assertEqual(asignatura.nombre, "Matemáticas")
        self.assertEqual(asignatura.codigo, "MAT101")

class AlumnoModelTests(TestCase):

    def test_alumno_creation(self):
        alumno = Alumno.objects.create(nombre="Juan", apellido_paterno="Perez", apellido_materno="Gomez", fecha_nacimiento="2000-01-01")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido_paterno, "Perez")
        self.assertEqual(alumno.apellido_materno, "Gomez")
        self.assertEqual(str(alumno), "Juan Perez Gomez")

class AsignaturaAlumnoModelTests(TestCase):

    def test_asignatura_alumno_creation(self):
        asignatura = Asignatura.objects.create(nombre="Matemáticas", codigo="MAT101")
        alumno = Alumno.objects.create(nombre="Juan", apellido_paterno="Perez", apellido_materno="Gomez", fecha_nacimiento="2000-01-01")
        asignatura_alumno = AsignaturaAlumno.objects.create(asignatura=asignatura, alumno=alumno)
        self.assertEqual(asignatura_alumno.asignatura, asignatura)
        self.assertEqual(asignatura_alumno.alumno, alumno)

class AsignaturaViewsTests(TestCase):

    def setUp(self):
        self.asignatura = Asignatura.objects.create(nombre="Matemáticas", codigo="MAT101")

    def test_listar_asignaturas(self):
        response = self.client.get(reverse('listar_asignaturas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Matemáticas")

