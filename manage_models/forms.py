from django import forms
from django.forms import fields, models
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2')
    
    def save(self):
        user = super(UserForm, self).save(commit=False)
        user.save()

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('telefono' , 'tipo_usuario')