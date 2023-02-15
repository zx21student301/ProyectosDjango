from django.urls import path
from .views import CamionListView, CamionDetailView, CamionCreateView, CamionDeleteView, CamionUpdateView
from . import views

urlpatterns = [
    path('',CamionListView.as_view(), name="listado"),
    path('detalles/<int:pk>', CamionDetailView.as_view(), name="detalles"),
    path('borrar/<int:pk>', CamionDeleteView.as_view(), name="borrar"),
    path('modificar/<int:pk>', CamionUpdateView.as_view(), name="modificar"),
    path('crear', CamionCreateView.as_view(), name="crear"),
    path('volver', views.volver, name='volver'),
]