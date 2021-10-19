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
]