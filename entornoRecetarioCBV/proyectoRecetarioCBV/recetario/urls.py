from django.urls import path
from .views import RecetaListView, RecetaDetailView, RecetaCreateView, RecetaDeleteView, RecetaUpdateView

urlpatterns = [
    path('',RecetaListView.as_view(), name="receta"),
    path('detalles/<int:pk>', RecetaDetailView.as_view(), name="detalles"),
    path('borrarReceta/<int:pk>', RecetaDeleteView.as_view(), name="borrarReceta"),
    path('modificarReceta/<int:pk>', RecetaUpdateView.as_view(), name="modificarReceta"),
    path('crearReceta', RecetaCreateView.as_view(), name="crearReceta"),
]