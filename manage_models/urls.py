from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name='home'),
    
    path('usuarios/' , views.usuarios, name='usuarios'),
    path('usuarios/registrar/' , views.registrar_usuario , name='registrar_usuario'),
    path('usuarios/borrar/<int:pk>' , views.borrar_usuario , name='borrar_usuario'),
    path('usuarios/editar/<int:pk>' , views.editar_usuario , name='editar_usuario'),
    path('usuarios/buscar/nombre/' , views.buscar_usuario_nombre , name='buscar_usuario_nombre'),
    path('usuarios/buscar/apellidos/' , views.buscar_usuario_apellidos , name='buscar_usuario_apellidos'),
    path('usuarios/buscar/email/' , views.buscar_usuario_email , name='buscar_usuario_email'),
    path('usuarios/buscar/telefono/' , views.buscar_usuario_telefono , name='buscar_usuario_telefono'),
    path('usuarios/buscar/tipo/' , views.buscar_usuario_tipo , name='buscar_usuario_tipo'),
    
    path('clientes/' , views.clientes , name='clientes'),
    path('clientes/registrar/' , views.registrar_cliente , name='registrar_cliente'),
    path('clientes/borrar/<int:pk>' , views.borrar_cliente , name='borrar_cliente'),
    path('clientes/editar/<int:pk>' , views.editar_cliente , name='editar_cliente'),
    path('clientes/buscar/nombre/' , views.buscar_cliente_nombre , name='buscar_cliente_nombre'),
    path('clientes/buscar/apellido/' , views.buscar_cliente_apellido , name='buscar_cliente_apellido'),
    path('clientes/buscar/email/' , views.buscar_cliente_email , name='buscar_cliente_email'),
    path('clientes/buscar/telefono/' , views.buscar_cliente_telefono , name='buscar_cliente_telefono'),
    path('clientes/buscar/rfc/' , views.buscar_cliente_rfc , name='buscar_cliente_rfc'),
    path('clientes/buscar/razon/' , views.buscar_cliente_razon , name='buscar_cliente_razon'),
    path('clientes/buscar/domicilio/' , views.buscar_cliente_domicilio , name='buscar_cliente_domicilio'),

    path('cajas/' , views.cajas , name='cajas'),
    path('cajas/administrar/' , views.cajas_lista , name='cajas_lista'),
    path('cajas/administrar/registrar/' , views.registrar_caja , name='registrar_caja'),
    path('cajas/administrar/borrar/<int:pk>' , views.borrar_caja , name='borrar_caja'),
    path('cajas/administrar/editar/<int:pk>' , views.editar_caja , name='editar_caja'),
    path('cajas/administrar/buscar/clave/' , views.buscar_caja_clave , name='buscar_caja_clave'),
]