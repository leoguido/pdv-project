from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('manage_models.urls')),
    path('' , include('ventas.urls')),
    path('accounts/login/', views.LoginView.as_view() , name='login'),
    path('accounts/login/', views.LogoutView.as_view(next_page='login') , name='logout'),
]
