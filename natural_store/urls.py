"""
URL configuration for natural_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from productos.views import ProductoListaView



urlpatterns = [
    #path('',  views.index, name= 'index'),
    #utilizar la clase como una vista
    path('',  ProductoListaView.as_view(), name= 'index'),
    path('usuarios/login',  views.login_vista, name= 'login'),
    path('usuarios/logout',  views.logout_vista, name= 'logout'),
    path('usuarios/registro',  views.registro, name= 'registro'),
    path('inventario/inventario',  views.inventario, name= 'inventario'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls'))
]
