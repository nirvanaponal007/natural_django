

from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return render (request, 'index.html' , {
        'mensaje': 'Hola Tio desde el mensaje',
        'titulo_empresa': 'Natural Star B',
        'productos':[
            {'titulo':'Shampoo Coco','precio':35000,'inventario': True},
            {'titulo':'Shampoo Manzana','precio':45000,'inventario': True},
            {'titulo':'Shampoo Pera','precio':37000,'inventario': False},
        ]
    })