from django import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioCrearFormConEmail


# Create your views here.
class RegistroView(CreateView):
    form_class = UsuarioCrearFormConEmail
    template_name = 'registration/registro.html'


    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?registrado'


    def get_form(self, form_class = None):
        form = super(RegistroView, self).get_form()


        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nombre'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'email'})
        form.fields['password1'].widget = forms.TextInput(attrs={'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'placeholder':'Contraseña'})


        return form