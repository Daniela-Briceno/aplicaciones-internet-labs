from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='alumnos')
    id = models.AutoField(primary_key=True) 
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

"""
Los modelos (Asignatura y Alumno) representan entidades 
en una base de datos Django y están diseñados para 
almacenar información sobre asignaturas y alumnos, respectivamente. 
"""
