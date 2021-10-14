from django.shortcuts import get_object_or_404, redirect, render , HttpResponse
from .models import Usuario
from .forms import UserForm , UsuarioForm
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Usuario, pk=request.user.id)  # Error. No encuentra el id de los usuarios creados
        return render(request, 'home/home.html' , {'user': user})
    else:
        return redirect('login')

def usuarios(request):
    return render(request , 'manage_models/usuarios.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            form1.save()
            form2 = UsuarioForm(request.POST , instance=Usuario.objects.get(usuario=User.objects.get(username=request.POST['username'])))
            if form2.is_valid():
                form2.save()
            return redirect('home')
        else:
            HttpResponse('PUTA ZORRA NOOOOOOOOOOOOOOOO')
    else:
        form1 = UserForm()
        form2 = UsuarioForm()
        return render(request , 'manage_models/usuarios_reg.html' , {'user_form1' : form1 , 'user_form2' : form2})