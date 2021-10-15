from django.shortcuts import get_object_or_404, redirect, render , HttpResponse
from .models import Usuario
from .forms import UserForm , UsuarioForm
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        return render(request, 'home/home.html' , {'user': user})
    else:
        return redirect('login')

def usuarios(request):
    users = User.objects.all()
    return render(request , 'manage_models/usuarios.html' , {'usuarios':users})

def registrar_usuario(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            form1.save()
            form2 = UsuarioForm(request.POST , instance=Usuario.objects.get(usuario=User.objects.get(username=request.POST['username'])))
            if form2.is_valid():
                form2.save()
            return redirect('usuarios')
    else:
        form1 = UserForm()
        form2 = UsuarioForm()
        return render(request , 'manage_models/usuarios_reg.html' , {'user_form1' : form1 , 'user_form2' : form2})

def borrar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.delete()
    return redirect('usuarios')

def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form1 = UserForm(request.POST , instance=usuario)
        if form1.is_valid():
            usuario = form1.save()
            form2 = UsuarioForm(request.POST , instance=Usuario.objects.get(usuario=User.objects.get(username=request.POST['username'])))
            if form2.is_valid():
                usuario = form2.save()
            return redirect('usuarios')
    else:
        form1 = UserForm(instance=usuario)
        form2 = UsuarioForm(instance=usuario)
        return render(request, 'manage_models/usuarios_edit.html' , {'user_form1' : form1 , 'user_form2' : form2})
