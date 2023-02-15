from django.urls import path
from . import views

urlpatterns = [
    path('', views.proposito, name="proposito"),
    path('nuevo',views.nuevo, name="nuevo"),
    path('borrar/<int:identificador>', views.borrar, name='borrar'),
    path('conseguido/<int:identificador>', views.conseguido, name='conseguido'),
    path('editar', views.editar, name='editar'),
    path('reiniciar/<int:identificador>', views.reiniciar, name='reiniciar'),
    path("aplazar", views.aplazar, name="aplazar"),
]