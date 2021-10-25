from django.contrib import admin
from .models import Marca ,Caja, CorteCaja, Producto, Categoria

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Categoria)