from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
from .models import Gender, Movies

def index(request):
    return render(request, 'index.html')

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
'''
def lista_movies(request):
    data = getMovies()
    peliculas = []

    for pelicula in data:
        pelicula_procesada = {
            'nombre': pelicula['name'],
            'resumen': pelicula['description'],
            'imagen': pelicula['poster'],
            'genero': pelicula['id'],
        }
        peliculas.append(pelicula_procesada)
    print(peliculas[0])
    return render(request, 'index.html', {'movies': peliculas})
    
def getMovies():
    url = "https://api.filmon.com/api/vod/search?"
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

'''