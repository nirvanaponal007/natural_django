from django.urls import path
from . import views

app_name = 'carritos'

urlpatterns = [
    path('', views.carro, name='carrito'),
    path('agregar', views.add, name='add')
]