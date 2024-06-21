

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import FormularioRegistro
from django.contrib.auth.models import User

def index (request):
    return render (request, 'index.html' , {
        'mensaje': 'Estas en Index!',
        'titulo_empresa': 'Natural Star B',
        'productos':[
            {'titulo':'Shampoo Coco','precio':35000,'inventario': True},
            {'titulo':'Shampoo Manzana','precio':45000,'inventario': True},
            {'titulo':'Shampoo Pera','precio':37000,'inventario': False},
        ]
    })


def login_vista (request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')

        user = authenticate(username=nombre_usuario, password=contraseña)
        if user:
            login(request, user)
            messages.success(request, 'Hola {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Contraseña no valida')


    return render (request, 'usuarios/login.html', {}
    )


def  logout_vista (request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('login')


def registro (request):
    form = FormularioRegistro(request.POST or None)

    if request.method == 'POST' and form.is_valid():
      

        user = form.save()

        if user:
            messages.success(request, 'Usuario creado correctamente')
            return redirect('index')




    return render(request, 'usuarios/registro.html', {
        'form': form
    })