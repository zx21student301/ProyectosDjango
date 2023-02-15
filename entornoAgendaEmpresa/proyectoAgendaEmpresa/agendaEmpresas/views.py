#from django.shortcuts import get_list_or_404, render
from .models import Empresa
from django.urls import reverse_lazy
#from django.template import loader
#from django.http import HttpResponse

from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
# Create your views here.

class EmpresaListView(ListView):
    model = Empresa

class EmpresaDetailView(DetailView):
    model = Empresa

class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nombre','tipo','direccion','telefono','personaContacto']
    success_url = reverse_lazy('listado')
    """ = """
    """def get_success_url(self):
        return reverse('listado')"""

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('listado')

class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['nombre','tipo','direccion','telefono','personaContacto']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')