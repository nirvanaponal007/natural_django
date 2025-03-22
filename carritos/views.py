from django.shortcuts import render
from .models import Carro
from productos.models import Producto
from .utils import obtener_o_crear_carrito

def carro(request):
    carro = obtener_o_crear_carrito(request)
    return render(request, 'carritos/carrito.html',{ 
    })

def add(request):
    carrito = obtener_o_crear_carrito(request)
    producto = Producto.objects.get(pk=request.POST.get('producto_id'))
    carrito.productos.add(producto)

    return render(request, 'carritos/add.html', {
        'producto': producto
    })

