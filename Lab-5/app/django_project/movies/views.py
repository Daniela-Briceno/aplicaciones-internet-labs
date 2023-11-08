from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
from .models import Gender, Movies

def index(request):
    return render(request, 'index.html')

# SE DEBE UNIR LA FUNCION LISTA_GENEROS CON LISTA_MOVIES

def lista_generos(request):
    print('ESTOY EN LISTA GENEROS')

    data = getGender()
    generos = []

    for genero in data:
        genero_procesado = {
            'identificacion': genero['id'],
            'genero': genero['name'],
        }
        generos.append(genero_procesado)

    if request.method == 'POST':
        genero_seleccionado = request.POST.get('genero')

        if genero_seleccionado:
            # Llama a la función getMovies con el género seleccionado y obtén las películas procesadas
            peliculas = getMovies(genero_seleccionado)
        else:
            # Si no se ha seleccionado un género, muestra todas las películas de deportes
            peliculas = getMovies('sports')
    else:
        # Por defecto, muestra todas las películas de deportes
        peliculas = getMovies('sports')

    return render(request, 'index.html', {'movies': peliculas, 'generos': generos})

def getMovies(genero_seleccionado):
    # Construye la URL de la API con el género seleccionado
    url = f"http://api.filmon.com/api/vod/search?genre={genero_seleccionado.lower()}"
    print(url)
    print('ESTOY EN GET MOVIES')
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer tu_token_de_autenticacion"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        peliculas = []

        for pelicula in data.get("response", []):
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

        return peliculas
    else:
        return []  # En caso de error, devuelve una lista vacía

 
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
