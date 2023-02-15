from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Receta
from django.urls import reverse_lazy
from .forms import RecetaForm

# Create your views here.
class RecetaListView(ListView):
    model = Receta

class RecetaDetailView(DetailView):
    model = Receta

class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    success_url = reverse_lazy('receta')

class RecetaDeleteView(DeleteView):
    model = Receta
    success_url = reverse_lazy('receta')

class RecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('receta')