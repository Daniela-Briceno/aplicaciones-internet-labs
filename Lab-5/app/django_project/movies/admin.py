from django.contrib import admin
from .models import Gender, Movies

class GenderAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'genero')

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'imagen', 'genero')

admin.site.register(Gender, GenderAdmin) 
admin.site.register(Movies, MoviesAdmin)