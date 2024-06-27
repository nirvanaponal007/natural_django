
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Producto

# creacion de la clase


class ProductoListaView(ListView):
    template_name = 'index.html'
    queryset= Producto.objects.all().order_by('-id')
    #despues de creado la vista, se debe ajustar URL

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['mensaje'] = 'Listado de productos Shampoo'
        contexto['Productos'] = contexto ['object_list']
        return contexto
    

class ProductoDetalleView(DetailView):
    #primero indicar el modelo
    model = Producto
    template_name = 'productos/producto.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        print(contexto)
        return contexto