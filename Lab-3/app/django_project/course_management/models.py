from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'

class AsignaturaAlumno(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.asignatura.nombre} - {self.alumno.nombre}'

