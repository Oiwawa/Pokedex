from django.shortcuts import render
from django.http.response import HttpResponse
import requests, os

from pokedexapp.models import Pokemon

def index(request):
    return render(request, "index.html")

def listPokemon(request):
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    result = r.json()
    result = result["results"]

    list1 = []
    listIndex = []
    index = 0
    for i in result:
        pokemon = i['name']
        list1.append(pokemon)
        listIndex.append(index)
        index += 1

    pokemons = zip(list1)
    context = {
        'pokemons': pokemons,
        'i': listIndex
    }
    return render(request, "listPokemon.html", context)
