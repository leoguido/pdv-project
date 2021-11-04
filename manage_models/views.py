from django.shortcuts import get_object_or_404, redirect, render , HttpResponse
from .models import Usuario , Cliente , Caja
from .forms import UserForm , UsuarioForm, ClienteForm, CajaForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json


def home(request):
    if request.user.is_authenticated:
        print('hola')
        user = get_object_or_404(User, pk=request.user.id)
        request.session['cajero'] = 'leo'
        return render(request, 'home/home.html' , {'user': user})
    else:
        return redirect('login')

@login_required
def usuarios(request):
    users = User.objects.all()
    return render(request , 'manage_models/usuarios.html' , {'usuarios':users})

@login_required
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

@login_required
def borrar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.delete()
    return redirect('usuarios')

@login_required
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
        form2 = UsuarioForm(instance=usuario.details)
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

@login_required
def clientes(request):
    clientes_lista = Cliente.objects.all()
    return render(request, 'manage_models/clientes.html' , {'clientes':clientes_lista})

@login_required
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
        return render(request , 'manage_models/clientes_reg.html' , {'form':form})

@login_required
def borrar_cliente(request , pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('clientes')

@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'manage_models/clientes_edit.html' , {'form':form})

def buscar_cliente_nombre(request):
    print(request.GET)
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(nombre__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

def buscar_cliente_apellido(request):
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(apellido__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

def buscar_cliente_email(request):
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(correo_electronico__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

def buscar_cliente_telefono(request):
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(telefono__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

def buscar_cliente_rfc(request):
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(rfc__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

def buscar_cliente_razon(request):
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(razon_social__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

def buscar_cliente_domicilio(request):
    data = request.GET['busqueda']
    clientes_filtrados_nombre =  Cliente.objects.filter(domicilio__icontains=data)
    clientes_nombres = []
    for cliente in clientes_filtrados_nombre:
        datos = {}
        datos['nombre'] = cliente.nombre
        datos['apellido'] = cliente.apellido
        datos['rfc'] = cliente.rfc
        datos['correo_electronico'] = cliente.correo_electronico
        datos['telefono'] = cliente.telefono
        datos['razon_social'] = cliente.razon_social
        datos['pk'] = cliente.pk
        datos['domicilio'] = cliente.domicilio
        clientes_nombres.append(datos)

    return HttpResponse(json.dumps(clientes_nombres) , 'application/json')

@login_required
def cajas(request):
    return render(request, 'manage_models/cajas.html')

@login_required
def cajas_lista(request):
    cajas_data = Caja.objects.all()
    return render(request, 'manage_models/cajas_lista.html' , {'cajas':cajas_data})

@login_required
def registrar_caja(request):
    if request.method == 'POST':
        form = CajaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cajas_lista')
    else:
        form = CajaForm()
        return render(request, 'manage_models/cajas_reg.html' , {'form':form})

@login_required
def borrar_caja(request, pk):
    caja = get_object_or_404(Caja, pk=pk)
    caja.delete()
    return redirect('cajas_lista')

@login_required
def editar_caja(request, pk):
    caja = get_object_or_404(Caja, pk=pk)
    if request.method == 'POST':
        form = CajaForm(request.POST , instance=caja)
        if form.is_valid():
            form.save()
            return redirect('cajas_lista')
    else:
        form = CajaForm(instance=caja)
        return render(request, 'manage_models/cajas_edit.html', {'form':form})

def buscar_caja_clave(request):
    data = request.GET['busqueda']
    cajas_filtradas_nombre =  Caja.objects.filter(clave__icontains=data)
    cajas_nombres = []
    for caja in cajas_filtradas_nombre:
        datos = {}
        datos['clave'] = caja.clave
        datos['nombre'] = caja.nombre
        datos['pk'] = caja.pk
        cajas_nombres.append(datos)

    return HttpResponse(json.dumps(cajas_nombres) , 'application/json')

def buscar_caja_nombre(request):
    data = request.GET['busqueda']
    cajas_filtradas_nombre =  Caja.objects.filter(nombre__icontains=data)
    cajas_nombres = []
    for caja in cajas_filtradas_nombre:
        datos = {}
        datos['clave'] = caja.clave
        datos['nombre'] = caja.nombre
        datos['pk'] = caja.pk
        cajas_nombres.append(datos)

    return HttpResponse(json.dumps(cajas_nombres) , 'application/json')
