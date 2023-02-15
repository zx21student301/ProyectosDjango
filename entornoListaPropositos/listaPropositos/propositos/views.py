from django.shortcuts import render
from .models import Propositos
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
import time
#alert que avisa de que el tiempo de plazo sale del año, para poder verlo ejecutar "pip install pyautogui" 
import pyautogui as pag
# Create your views here.
def proposito(request):
    lp = Propositos.objects.all()
    context = {
        'proposito': lp,
    }
    plantilla = loader.get_template('index.html')
    return HttpResponse(plantilla.render(context,request))

def nuevo(request):
    p = request.GET['proposito']
    fo = request.GET['fechaObjetivo']

    prop = Propositos(proposito = p, fechaObjetivo= fo, conseguido = False)
    prop.save()

    return HttpResponseRedirect(reverse('proposito'))

def borrar(request,identificador):
    Propositos.objects.filter(id=identificador).delete()

    return HttpResponseRedirect(reverse('proposito'))

def conseguido(request, identificador):
    fr = datetime.now()

    ob = Propositos.objects.get(id=identificador)

    ob.fechaConseguido = fr
    ob.conseguido = True
    ob.save()

    return HttpResponseRedirect(reverse('proposito'))

def editar(request):
    idp = request.GET['idPropositoE']

    ob = Propositos.objects.get(id=idp)

    np = request.GET['propositoNuevo']
    nfo = request.GET['fechaObjetivoNuevo']

    ob.proposito = np
    ob.fechaObjetivo = nfo
    ob.save()

    return HttpResponseRedirect(reverse('proposito'))

def reiniciar(request, identificador):
    ob = Propositos.objects.get(id=identificador)

    ob.conseguido = False
    ob.save()

    return HttpResponseRedirect(reverse('proposito'))

def aplazar(request):
    idp = request.GET['idPropositoA']

    ob = Propositos.objects.get(id=idp)

    diasSum = request.GET['aplazo']

    fechaOb = ob.fechaObjetivo

    nuevaFechaOb = fechaOb + timedelta(days = int(diasSum))

    fechaObStr = nuevaFechaOb.strftime("%Y%m%d")
    fechaLim = "20231231"

    if time.strptime(fechaObStr, "%Y%m%d") > time.strptime(fechaLim, "%Y%m%d"):
        ob.fechaObjetivo =  "2023-12-31"

        # Message Box
        pag.alert(text="Como tu aplazo se ha salido del 2023, la nueva fecha es 31-12-2023", title="Alerta")
    else:
        ob.fechaObjetivo = nuevaFechaOb

    ob.conseguido = False
    ob.save()

    return HttpResponseRedirect(reverse('proposito'))