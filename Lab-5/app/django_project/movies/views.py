from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
from .models import Gender, Movies

def index(request):
    return render(request, 'index.html')

# SE DEBE UNIR LA FUNCION LISTA_GENEROS CON LISTA_MOVIES

def lista_generos(request):
    data = getGender()
    print(data)
    generos = []

    for genero in data:
        genero_procesado = {
            'identificacion': genero['id'],
            'genero': genero['name'],
        }
        generos.append(genero_procesado)
    print(generos[0])
    return render(request, 'index.html', {'generos': generos})
    
def getGender():
    url = "https://api.filmon.com/api/vod/genres"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWJjN2I0N2I4OWM1MDdhZWUwYjJmMjliOGEyMmU4NSIsInN1YiI6IjY1MzlhM2RmOTU1YzY1MDExYmUwYzhkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cuKI41__m1E2SBGXAf3qGLVHq9vqnmcyTAYrO_11MwU"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("response", [])  # Devuelve la lista de generos
    else:
        return []  # Devuelve una lista vacía en caso de error

def lista_movies(request):
    data = getMovies()
    peliculas = []

    for pelicula in data:
        nombre = pelicula.get('title', 'Nombre no disponible')
        resumen = pelicula.get('description', 'Descripción no disponible')
        
        poster = pelicula.get('poster', {})
        imagen = poster.get('url', 'URL no disponible')
        
        pelicula_procesada = {
            'nombre': nombre,
            'resumen': resumen,
            'imagen': imagen,
        }
        peliculas.append(pelicula_procesada)
    print(peliculas[0])
    return render(request, 'index.html', {'movies': peliculas})
    
def getMovies():
    # AQUÍ, SE DEBE RECIBIR POR PARÁMERO EL GENERO
    # ASÍ PODER REMPLAZAR EL VALOR DEL GENERO EN EL URL Y VOLVERLO DINAMICO
    url = "http://api.filmon.com/api/vod/search?genre=sports"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWJjN2I0N2I4OWM1MDdhZWUwYjJmMjliOGEyMmU4NSIsInN1YiI6IjY1MzlhM2RmOTU1YzY1MDExYmUwYzhkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cuKI41__m1E2SBGXAf3qGLVHq9vqnmcyTAYrO_11MwU"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("response", [])
    else:
        return []  

