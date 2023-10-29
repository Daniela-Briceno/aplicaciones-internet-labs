from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
from .models import Movie

def index(request):
#    courses = Course.objects.all()
    return render(request, 'index.html')

def lista_movies(request):
    data = getMovies()
    # Crear una lista vacía para almacenar los datos procesados
    peliculas = []
    # Recorrer los datos de películas y crear una estructura de datos para cada película
    for pelicula in data:
        pelicula_procesada = {
            'titulo': pelicula['title'],
            'resumen': pelicula['overview'],
            'fecha': pelicula['release_date'],
            'imagen': pelicula['poster_path'],
            'calificacion': pelicula['vote_average'],
            'vote_count': pelicula['vote_count']
        }
        peliculas.append(pelicula_procesada)
    print(peliculas[0])
    return render(request, 'index.html', {'movies': peliculas})
    
def getMovies():
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWJjN2I0N2I4OWM1MDdhZWUwYjJmMjliOGEyMmU4NSIsInN1YiI6IjY1MzlhM2RmOTU1YzY1MDExYmUwYzhkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cuKI41__m1E2SBGXAf3qGLVHq9vqnmcyTAYrO_11MwU"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])  # Devuelve la lista de películas
    else:
        return []  # Devuelve una lista vacía en caso de error

