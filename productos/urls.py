from django.urls import path
from . import views

#llave utilizada

urlpatterns = [
    path('buscador', views.ProductoBuscadorView.as_view(), name='buscador'),
    path('<slug:slug>', views.ProductoDetalleView.as_view(), name='producto'),
    
    
    
]