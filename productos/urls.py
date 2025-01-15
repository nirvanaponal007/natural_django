from django.urls import path
from . import views

#llave utilizada

urlpatterns = [
    path('<slug:slug>', views.ProductoDetalleView.as_view(), name='producto')
]