from django import forms
from .models import Camion

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['marca','modelo','imagen','descripcion','precio','author','categorias']
        widgets = {
            'marca': forms.TextInput(attrs={"style":'margin-top:10px; margin-bottom:10px; padding: 2px 2px;'}),
            'modelo': forms.TextInput(attrs={"style":'margin-top:10px; margin-bottom:10px; padding: 2px 2px;'}),
            'descripcion': forms.Textarea(attrs={"style":'margin-top:10px; margin-bottom:10px; padding: 2px 2px;'}),
            'precio': forms.TextInput(attrs={"style":'margin-top:10px; margin-bottom:10px; padding: 2px 2px;'})
        }