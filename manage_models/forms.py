from django import forms
from django.forms import fields, models
from .models import Usuario , Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2')

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('telefono' , 'tipo_usuario')

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre' , 'apellido' , 'correo_electronico' , 'telefono' , 'rfc' , 'razon_social' , 'domicilio')