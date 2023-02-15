from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Camion
from django.urls import reverse, reverse_lazy
from .forms import CamionForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CamionListView(ListView):
    model = Camion

class CamionDetailView(DetailView):
    model = Camion

class CamionCreateView(LoginRequiredMixin,CreateView):
    login_url = '/cuentas/login/'
    model = Camion
    form_class = CamionForm
    success_url = reverse_lazy('listado')

class CamionDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/cuentas/login/'
    model = Camion
    success_url = reverse_lazy('listado')

class CamionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/cuentas/login/'
    model = Camion
    form_class = CamionForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

def volver(request):
    return HttpResponseRedirect(reverse('listado'))