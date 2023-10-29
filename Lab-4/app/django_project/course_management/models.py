from django.db import models

class Movie(models.Model):
    titulo = models.CharField(max_length=255)
    resumen = models.TextField()
    fecha = models.DateField()
    imagen = models.URLField()
    genero = models.CharField(max_length=255)
    calificacion = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo
