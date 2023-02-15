from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('receta',views.receta,name='receta'),
    path('desayunos',views.desayunos,name='desayunos'),
    path('comidas',views.comidas,name='comidas'),
    path('cenas',views.cenas,name='cenas'),
    path('todas',views.todas,name='todas'),
    path('categoria/<int:idCategoria>', views.categoria, name='categoria'),
]