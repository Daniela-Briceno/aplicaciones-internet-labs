from django.db import models

class Gender(models.Model):
    identificacion = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    
    def __str__(self):
        return self.identificacion

class Movies(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.URLField()
    genero = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
