from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from manage_models.models import Caja, CorteCaja , Usuario
from manage_models.forms import CorteForm , FinalCorteForm
from django.utils import timezone


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
