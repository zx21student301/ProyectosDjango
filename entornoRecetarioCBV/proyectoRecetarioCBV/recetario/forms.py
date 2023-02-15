from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre','subnombre','imagen','ingredientes','receta','author','categorias']
        #modificar los inputs
        widgets = {
            'nombre' : forms.TextInput(attrs={'style':'background-color:red'}),
            'subnombre' : forms.TextInput(attrs={'placeholder':'escribe el subnombre','style':'background-color:skyblue'}),
        }
        #modificar los labels
        labels = {
            'subnombre':'Sub nombre',
        }