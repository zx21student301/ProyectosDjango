from django.shortcuts import render
from .models import Receta,Categoria
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def inicio(request):
    home = loader.get_template('recetario/inicio.html')
    return HttpResponse(home.render())

def receta(request):
    receta = loader.get_template('recetario/receta.html')
    return HttpResponse(receta.render())

def desayuno(request):
    desayuno = loader.get_template('recetario/desayuno.html')
    return HttpResponse(desayuno.render())

def comida(request):
    comida = loader.get_template('recetario/comida.html')
    return HttpResponse(comida.render())

def cena(request):
    cena = loader.get_template('recetario/cena.html')
    return HttpResponse(cena.render())

def todas(request):
    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render())