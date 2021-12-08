from django.shortcuts import render
from django.http.response import HttpResponse
import requests, os

def index(request):
    return render(request, "index.html")

def listPokemon(request):
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    result = r.json()
    result = result["results"]

    list1 = []
    index = 0
    for name in result:
        list1.append(result[index]['name'])
        index += 1

    mylist = zip(list1)
    context = {
        'mylist': mylist,
    }
    return render(request, "listPokemon.html", context)
