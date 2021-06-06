from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.forms import models, widgets
from .models import Profile

"""
Ahora vamos a extender el formulario UserCreationForm que usaremos en views en la clase SignupView para que cuente con email:
"""
class UserCreationFormWidthEmail(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Requerido, 254 caracteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    #Vamos a añadir una validación al campo email para que no puedan haber más de un usuario con el mismo email:
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link'] 
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio' : forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link' : forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),

        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True,help_text="Requerido, 254 caracteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data: # changed_data es una lista que almacena los campos que se han modificado en el formulario.
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email