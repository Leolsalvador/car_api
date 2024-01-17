from django.contrib import admin
from django.urls import path
from usuarios.views import UsuariosView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', UsuariosView.as_view(), name='usuarios'),
]
