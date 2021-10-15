from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name='home'),
    path('usuarios/' , views.usuarios, name='usuarios'),
    path('usuarios/registrar/' , views.registrar_usuario , name='registrar_usuario'),
    path('usuarios/borrar/<int:pk>' , views.borrar_usuario , name='borrar_usuario'),
    path('usuarios/editar/<int:pk>' , views.editar_usuario , name='editar_usuario'),
]