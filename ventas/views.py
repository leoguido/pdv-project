from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from manage_models.models import Caja, CorteCaja , Usuario , Cliente, Producto, Venta, DetalleVenta
from manage_models.forms import CorteForm , FinalCorteForm
from django.utils import timezone
import json


def seleccion_caja(request):
    cajas = Caja.objects.all()
    return render(request, 'ventas/seleccionar_caja.html', {'cajas':cajas})

def usar_caja(request, pk):
    caja = get_object_or_404(Caja, pk=pk)
    if caja.estado == 'C':
        if request.method == 'POST':
            form = CorteForm(request.POST)
            corte = form.save(commit=False)
            corte.caja = caja
            corte.fecha_inicio = timezone.now()
            corte.usuario = get_object_or_404(Usuario, usuario=request.user)
            corte.save()
            return redirect('abrir_caja', pk=caja.pk)
        else:
            form = CorteForm()
            return render(request , 'ventas/abrir_caja.html', {'caja': caja , 'form':form})
    if caja.estado == 'A':
        cortes = CorteCaja.objects.filter(caja=caja).filter(fecha_cierre__isnull=True).filter(saldo_final__isnull=True)
        corte = get_object_or_404(CorteCaja, pk=cortes[0].pk)
        if request.method == 'POST':
            form = FinalCorteForm(request.POST, instance=corte)
            if form.is_valid():
                corte_final = form.save(commit=False)
                corte_final.fecha_cierre = timezone.now()
                corte_final.save()
                return redirect('cerrar_caja' , pk=caja.pk)
        else:
            form = FinalCorteForm()
            return render(request , 'ventas/usar_caja.html' ,{'caja': caja , 'corte':corte , 'form':form})

def abrir_caja(request, pk):
    caja = get_object_or_404(Caja, pk=pk)
    caja.estado = 'A'
    caja.save()
    return redirect('usar_caja' , pk=caja.pk)

def cerrar_caja(request, pk):
    caja = get_object_or_404(Caja, pk=pk)
    caja.estado = 'C'
    caja.save()
    return redirect('usar_caja' , pk=caja.pk)

def cortes_lista(request , pk):
    caja = get_object_or_404(Caja, pk=pk)
    cortes = CorteCaja.objects.filter(caja=caja)
    return render(request, 'ventas/cortes_lista.html', {'cortes':cortes , 'caja_actual':caja})

def venta(request, pk):
    caja = get_object_or_404(Caja, pk=pk)
    return render(request, 'ventas/venta.html' , {'caja':caja})

def get_clientes(request):
    clientes = Cliente.objects.all()
    clientes_nombre = []
    for cliente in clientes:
        clientes_nombre.append(cliente.razon_social)
    return HttpResponse(json.dumps(clientes_nombre) , 'application/json')

def get_productos(request):
    productos = Producto.objects.all()
    producto_nombre = []
    for producto in productos:
        producto_nombre.append(str(producto.nombre))
    return HttpResponse(json.dumps(producto_nombre) , 'application/json')

def get_producto(request):
    data = request.GET['producto']
    producto = get_object_or_404(Producto, nombre=data)
    producto_dict = {}
    producto_dict['nombre'] = producto.nombre
    producto_dict['precio'] = str(producto.precio)
    return HttpResponse(json.dumps(producto_dict) , 'application/json')

def registrar_venta(request):
    print(request.GET)
    data = json.loads(request.GET['json'])
    cliente = get_object_or_404(Cliente, razon_social=data['cliente'])
    caja = get_object_or_404(Caja, pk=data['caja'])
    usuario = get_object_or_404(Usuario, usuario=request.user)
    nueva_venta = Venta.objects.create(cliente=cliente, caja=caja, vendedor=usuario)
    for venta_ in data['ventas']:
        producto = get_object_or_404(Producto, nombre=venta_['productos'])
        producto.cantidad = producto.cantidad - int(venta_['cantidad_'])
        DetalleVenta.objects.create(venta=nueva_venta, cantidad = int(venta_['cantidad_']) , productos=producto, descuento = float(venta_['descuento_']), importe = float(venta_['importe_']), valor_unitario = producto.precio)
    return HttpResponse(Venta.objects.all())

def reportes_venta(request):
    ventas = Venta.objects.all()
    detalles = DetalleVenta.objects.all()
    return render(request, 'ventas/reportes_venta.html', {'ventas':ventas, 'detalles':detalles})