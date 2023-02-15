from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('receta',views.receta, name='receta'),
    path('desayuno',views.desayuno, name='desayuno'),
    path('cena',views.cena, name='cena'),
    path('comida',views.comida, name='comida'),
    path('todas',views.todas, name='todas'),
]