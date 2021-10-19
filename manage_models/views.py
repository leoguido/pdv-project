from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render , HttpResponse
from .models import Usuario
from .forms import UserForm , UsuarioForm, ClienteForm
from django.contrib.auth.models import User
from .models import Cliente
import json


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
        form2 = UsuarioForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            usuario1 = form1.save()
            usuario2 = form2.save(commit=False)
            usuario2.usuario = usuario1
            usuario2.save()
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

def buscar_usuario_nombre(request):
    data = request.GET['busqueda']
    usuarios_filtrados_nombre =  User.objects.filter(first_name__icontains=data)
    usuarios_nombres = []
    for usuario in usuarios_filtrados_nombre:
        datos = {}
        datos['first_name'] = usuario.first_name
        datos['last_name'] = usuario.last_name
        datos['username'] = usuario.username
        datos['email'] = usuario.email
        datos['telefono'] = usuario.details.telefono
        datos['tipo_usuario'] = usuario.details.tipo_usuario
        datos['pk'] = usuario.pk
        usuarios_nombres.append(datos)

    return HttpResponse(json.dumps(usuarios_nombres) , 'application/json')

def buscar_usuario_apellidos(request):
    data = request.GET['busqueda']
    usuarios_filtrados_nombre =  User.objects.filter(last_name__icontains=data)
    usuarios_nombres = []
    for usuario in usuarios_filtrados_nombre:
        datos = {}
        datos['first_name'] = usuario.first_name
        datos['last_name'] = usuario.last_name
        datos['username'] = usuario.username
        datos['email'] = usuario.email
        datos['telefono'] = usuario.details.telefono
        datos['tipo_usuario'] = usuario.details.tipo_usuario
        datos['pk'] = usuario.pk
        usuarios_nombres.append(datos)

    return HttpResponse(json.dumps(usuarios_nombres) , 'application/json')

def buscar_usuario_email(request):
    data = request.GET['busqueda']
    usuarios_filtrados_nombre =  User.objects.filter(email__icontains=data)
    usuarios_nombres = []
    for usuario in usuarios_filtrados_nombre:
        datos = {}
        datos['first_name'] = usuario.first_name
        datos['last_name'] = usuario.last_name
        datos['username'] = usuario.username
        datos['email'] = usuario.email
        datos['telefono'] = usuario.details.telefono
        datos['tipo_usuario'] = usuario.details.tipo_usuario
        datos['pk'] = usuario.pk
        usuarios_nombres.append(datos)

    return HttpResponse(json.dumps(usuarios_nombres) , 'application/json')

def buscar_usuario_telefono(request):
    data = request.GET['busqueda']
    usuarios_filtrados_nombre =  Usuario.objects.filter(telefono__icontains=data)
    usuarios_nombres = []
    for usuario in usuarios_filtrados_nombre:
        datos = {}
        datos['first_name'] = usuario.usuario.first_name
        datos['last_name'] = usuario.usuario.last_name
        datos['username'] = usuario.usuario.username
        datos['email'] = usuario.usuario.email
        datos['telefono'] = usuario.telefono
        datos['tipo_usuario'] = usuario.tipo_usuario
        datos['pk'] = usuario.usuario.pk
        usuarios_nombres.append(datos)

    return HttpResponse(json.dumps(usuarios_nombres) , 'application/json')

def buscar_usuario_tipo(request):
    data = request.GET['busqueda']
    usuarios_filtrados_nombre =  Usuario.objects.filter(tipo_usuario__icontains=data)
    usuarios_nombres = []
    for usuario in usuarios_filtrados_nombre:
        datos = {}
        datos['first_name'] = usuario.usuario.first_name
        datos['last_name'] = usuario.usuario.last_name
        datos['username'] = usuario.usuario.username
        datos['email'] = usuario.usuario.email
        datos['telefono'] = usuario.telefono
        datos['tipo_usuario'] = usuario.tipo_usuario
        datos['pk'] = usuario.usuario.pk
        usuarios_nombres.append(datos)

    return HttpResponse(json.dumps(usuarios_nombres) , 'application/json')

def clientes(request):
    clientes_lista = Cliente.objects.all()
    return render(request, 'manage_models/clientes.html' , {'clientes':clientes_lista})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
        return render(request , 'manage_models/clientes_reg.html' , {'form':form})
