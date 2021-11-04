from django.contrib import admin
from django.urls import path , include
from . import views
from pdv_project import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cajas/seleccionar/' , views.seleccion_caja, name='seleccionar_caja'),
    path('cajas/usar/<int:pk>' , views.usar_caja, name='usar_caja'),
    path('cajas/abrir/<int:pk>' , views.abrir_caja, name='abrir_caja'),
    path('cajas/cerrar/<int:pk>' , views.cerrar_caja, name='cerrar_caja'),

    path('cajas/usar/<int:pk>/historial/' , views.cortes_lista, name='cortes_lista'),
    path('cajas/usar/<int:pk>/venta/' , views.venta, name='venta'),
    path('clientes/data/nombres/' , views.get_clientes, name='clientes_namedata'),
    path('productos/data/nombres/' , views.get_productos, name='productos_namedata'),
    path('producto/get/nombre/' , views.get_producto, name='get_producto'),
    path('cajas/usar/venta/' , views.registrar_venta, name='registrar_venta'),
    path('cajas/usar/venta/descargar/' , views.descargar_venta, name='descargar_venta'),

    path('reportes/' , views.reportes_venta, name='reportes_venta'),
    path('reportes/buscar/' , views.buscar_venta, name='buscar_descuento'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)