from django.test import TestCase
from django.urls import reverse
from .models import Asignatura, Alumno

class AsignaturaModelTests(TestCase):
    def setUp(self):
        self.asignatura = Asignatura.objects.create(nombre='Matemáticas', codigo='MAT001')

    def test_asignatura_nombre(self):
        self.assertEqual(str(self.asignatura), self.asignatura.nombre)

class AlumnoModelTests(TestCase):
    def setUp(self):
        self.alumno = Alumno.objects.create(nombre='Juan', apellido_paterno='Perez', apellido_materno='Gomez', fecha_nacimiento='2000-01-01')

    def test_alumno_nombre_completo(self):
        self.assertEqual(str(self.alumno), 'Juan Perez Gomez')

class AsignaturaAlumnoTests(TestCase):
    def setUp(self):
        self.asignatura = Asignatura.objects.create(nombre='Física', codigo='FIS001')
        self.alumno = Alumno.objects.create(nombre='Maria', apellido_paterno='Lopez', apellido_materno='Gonzalez', fecha_nacimiento='1999-05-15')

    def test_agregar_alumno_a_asignatura(self):
        asignatura_alumno = AsignaturaAlumno.objects.create(asignatura=self.asignatura, alumno=self.alumno)
        self.assertEqual(asignatura_alumno.asignatura, self.asignatura)
        self.assertEqual(asignatura_alumno.alumno, self.alumno)

class AsignaturaAlumnoViewsTests(TestCase):
    def setUp(self):
        self.asignatura = Asignatura.objects.create(nombre='Historia', codigo='HIS001')
        self.alumno = Alumno.objects.create(nombre='Carlos', apellido_paterno='Gomez', apellido_materno='Fernandez', fecha_nacimiento='2002-09-20')

    def test_lista_asignaturas_alumnos(self):
        response = self.client.get(reverse('lista_asignaturas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.asignatura.nombre)
        self.assertContains(response, self.alumno.nombre)

    def test_detalle_asignatura(self):
        response = self.client.get(reverse('detalle_asignatura', args=[self.asignatura.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.asignatura.nombre)

