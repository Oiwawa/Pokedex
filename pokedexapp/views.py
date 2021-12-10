from django.shortcuts import render
from django.http.response import HttpResponse
import requests

from pokedexapp.models import Pokemon

def index(request):
    return render(request, "index.html")

def listPokemon(request):
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    results = r.json()
    
    list1 = []
    pokemon_name = []
    pokemon_img = []
    for i in results['results']:
        list1.append(i['url'])
        pokemon_name.append(i['name'])

    for j in list1:
        request_info = requests.get(j)
        info = request_info.json()
        img = info['sprites']['front_shiny']
        pokemon_img.append(img)

    pokemons = zip(pokemon_name, pokemon_img)
    context = {
        'pokemons': pokemons,
    }
    return render(request, "listPokemon.html", context)
