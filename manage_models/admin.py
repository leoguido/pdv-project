from django.contrib import admin
from .models import Marca, Producto, Categoria, Caja, CorteCaja

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Caja)
admin.site.register(CorteCaja)