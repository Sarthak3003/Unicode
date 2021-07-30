from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    url= requests.get('https://pokeapi.co/api/v2/type/')
    result= url.json()
    return render(request, 'index.html', {'url': result})
