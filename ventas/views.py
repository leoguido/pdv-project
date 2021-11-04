from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from manage_models.models import Caja, CorteCaja , Usuario , Cliente, Producto, Venta, DetalleVenta
from manage_models.forms import CorteForm , FinalCorteForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import json, pyexcel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@login_required
def seleccion_caja(request):
    cajas = Caja.objects.all()
    return render(request, 'ventas/seleccionar_caja.html', {'cajas':cajas})

@login_required
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

@login_required
def cortes_lista(request , pk):
    caja = get_object_or_404(Caja, pk=pk)
    cortes = CorteCaja.objects.filter(caja=caja)
    return render(request, 'ventas/cortes_lista.html', {'cortes':cortes , 'caja_actual':caja})

@login_required
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
    data = json.loads(request.GET['json'])
    cliente = get_object_or_404(Cliente, razon_social=data['cliente'])
    caja = get_object_or_404(Caja, pk=data['caja'])
    usuario = get_object_or_404(Usuario, usuario=request.user)
    nueva_venta = Venta.objects.create(cliente=cliente, caja=caja, vendedor=usuario)

    c = canvas.Canvas('Files/recibo.pdf', pagesize=letter)
    c.setFont('Helvetica',25)
    c.drawString(200,750, 'EMPRESA SA DE CV')
    c.setFont('Helvetica',15)
    c.drawString(260,730, 'Recibo de pago')
    c.line(200,725, 450,725)
    c.setFont('Helvetica',10)
    c.drawString(200,710, 'Cliente: ')
    c.drawString(240,710, cliente.razon_social)
    lista = c.beginText(200,670)
    lista.setFont('Helvetica',10)

    for venta_ in data['ventas']:
        producto = get_object_or_404(Producto, nombre=venta_['productos'])
        producto.cantidad = producto.cantidad - int(venta_['cantidad_'])
        DetalleVenta.objects.create(venta=nueva_venta, cantidad = int(venta_['cantidad_']) , productos=producto, descuento = float(venta_['descuento_']), importe = float(venta_['importe_']), valor_unitario = producto.precio)

        lista.textLine(producto.nombre + ' x' + str(venta_['cantidad_']) + '  -----  ' + str(venta_['importe_']) )
    
    lista.textLine('')
    lista.textLine('Total  -----  ' + str(data['total']))
    c.drawText(lista)
    c.drawString(260,50, 'Gracias por comprar!')
    c.showPage()
    c.save()

    return HttpResponse(Venta.objects.all())

def descargar_venta(request):
    recibo = open('Files/recibo.pdf', 'rb')
    response = FileResponse(recibo)
    return response

@login_required
def reportes_venta(request):
    ventas = Venta.objects.all()
    detalles = DetalleVenta.objects.all()
    excel_dict = []
    for detalle in detalles:
        data = {}
        data['producto'] = detalle.productos.nombre
        data['fecha'] = str(detalle.venta.fecha_venta)
        data['cliente'] = detalle.venta.cliente.razon_social
        data['vendedor'] = detalle.venta.vendedor.usuario.username
        data['caja'] = detalle.venta.caja.nombre
        data['cantidad'] = detalle.cantidad
        data['valor_unitario'] = detalle.productos.precio
        data['descuento'] = detalle.descuento
        data['importe'] = detalle.importe
        excel_dict.append(data)
    pyexcel.save_as(records=excel_dict,dest_file_name="Files/reporte_ventas.xls")

    return render(request, 'ventas/reportes_venta.html', {'ventas':ventas, 'detalles':detalles})

def buscar_venta(request):
    filtros = {}
    data = json.loads(request.GET['datos'])
    print(data)
    for campo, valor in data.items():
        if valor:
            if campo in ['productos__nombre','venta__cliente__razon_social','venta__vendedor__usuario__username','venta__caja__nombre']:
                filtros['%s__icontains'%campo] = data[campo]
            if campo in ['cantidad' , 'descuento']:
                filtros['%s__iexact'%campo] = data[campo]
            if campo in ['venta__fecha_venta', 'productos__precio', 'importe']:
                if not data[campo][0] == '' or not data[campo][1] == '':
                    filtros['%s__range'%campo] = [data[campo][0], data[campo][1]]
    ventas_filtradas_cliente =  DetalleVenta.objects.filter(**filtros)
    ventas_nombres = []
    for venta in ventas_filtradas_cliente:
        datos = {}
        datos['productos'] = venta.productos.nombre
        datos['fecha_venta'] = str(venta.venta.fecha_venta)
        datos['cliente'] = venta.venta.cliente.razon_social
        venta_object = venta.venta
        nombre = venta_object.vendedor.usuario.username
        datos['vendedor'] = nombre
        datos['caja'] = venta.venta.caja.nombre
        datos['cantidad'] = int(venta.cantidad)
        datos['valor_unitario'] = float(venta.productos.precio)
        datos['descuento'] = float(venta.descuento)
        datos['importe'] = float(venta.importe)
        ventas_nombres.append(datos)
    if len(ventas_nombres) >= 1:
        pyexcel.save_as(records=ventas_nombres, dest_file_name="Files/reporte_ventas.xls")
    else:
        detalles = DetalleVenta.objects.all()
        excel_dict = []
        for detalle in detalles:
            data = {}
            data['producto'] = detalle.productos.nombre
            data['fecha'] = str(detalle.venta.fecha_venta)
            data['cliente'] = detalle.venta.cliente.razon_social
            data['vendedor'] = detalle.venta.vendedor.usuario.username
            data['caja'] = detalle.venta.caja.nombre
            data['cantidad'] = detalle.cantidad
            data['valor_unitario'] = detalle.productos.precio
            data['descuento'] = detalle.descuento
            data['importe'] = detalle.importe
            excel_dict.append(data)
        pyexcel.save_as(records=excel_dict,dest_file_name="Files/reporte_ventas.xls")
    return HttpResponse(json.dumps(ventas_nombres) , 'application/json')