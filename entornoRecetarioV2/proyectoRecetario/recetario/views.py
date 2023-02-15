from django.shortcuts import get_list_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import Receta
# Create your views here.
def inicio(request):
    home = loader.get_template('recetario/inicio.html')
    return HttpResponse(home.render())

def receta(request):

    receta = Receta.objects.filter().order_by('-id')[0]

    ctx = {
        'receta' : receta
    }

    receta = loader.get_template('recetario/receta.html')
    return HttpResponse(receta.render(ctx, request))

def desayunos(request):

    receta = Receta.objects.filter(categorias__nombre="desayuno")

    ctx = {
        'receta' : receta
    }   

    desayunos = loader.get_template('recetario/desayunos.html')
    return HttpResponse(desayunos.render(ctx,request))

def comidas(request):

    receta = Receta.objects.filter(categorias__nombre="comida")

    ctx = {
        'receta' : receta
    }

    comidas = loader.get_template('recetario/comidas.html')
    return HttpResponse(comidas.render(ctx,request))

def cenas(request):

    receta = Receta.objects.filter(categorias__nombre="cena")

    ctx = {
        'receta' : receta
    }

    cenas = loader.get_template('recetario/cenas.html')
    return HttpResponse(cenas.render(ctx,request))

def todas(request):

    recetas = get_list_or_404(Receta)

    ctx = {
        'recetas' : recetas
    }

    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render(ctx,request))

def categoria(request, idCategoria):
    recetas = get_list_or_404(Receta, categorias = idCategoria)

    ctx = {
        'recetas' : recetas
    }

    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render(ctx,request))