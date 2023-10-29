from django.contrib import admin
from .models import Movie

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('titulo','resumen', 'fecha', 'imagen', 'genero', 'calificacion')

admin.site.register(Movie, MoviesAdmin)