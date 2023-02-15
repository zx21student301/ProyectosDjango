from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioCrearFormConEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obligatorio. 254 caracteres y un email valido")

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def clean_email(self):
        correo = self.cleaned_data.get("email")

        #comprobar que el email no existe
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError("Error: el correo ya está registrado.")

        return correo