from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Caja(models.Model):
    clave = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    marca = models.ForeignKey(Marca, null=True, blank=True, on_delete=models.RESTRICT)
    categoria = models.ManyToManyField(Categoria, blank=True)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)



TIPOS_USUARIO = (('A', 'ADMINISTRADOR'), ('V', 'VENDEDOR'))

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE , related_name='details')
    telefono = models.CharField(max_length=10)
    tipo_usuario = models.CharField(choices=TIPOS_USUARIO, max_length=1)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(null=True)
    telefono = models.CharField(max_length=10)
    rfc = models.CharField(max_length=13, default='')
    razon_social = models.CharField(max_length=100, default='')
    domicilio = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.razon_social

class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.RESTRICT)    
    vendedor = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.RESTRICT)
    caja = models.ForeignKey(Caja, null=False, blank=False, on_delete=models.RESTRICT)
    
    
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    productos = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    importe = models.DecimalField(max_digits=6, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=5, decimal_places=2)

ESTADO = (('A', 'Abierta'), ('C', 'Cerrada'))

class CorteCaja(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_cierre = models.DateTimeField(null=True, blank=True, auto_now_add=False, auto_now=False)
    saldo_inicial = models.DecimalField(max_digits=6, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.CharField(choices=ESTADO, max_length=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)