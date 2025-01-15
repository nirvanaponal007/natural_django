

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import FormularioRegistro
from django.contrib.auth.models import User
#importamos producto
from productos.models import Producto

def index (request):


    #crear variable
    productos = Producto.objects.all().order_by('-id')


    return render (request, 'index.html' , {
        'mensaje': 'Estas en Index!',
        'titulo_empresa': 'Natural Star B',
        'Productos':productos
    })


def login_vista (request):
    if request.user.is_authenticated:
        return redirect('index') 

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
    if request.user.is_authenticated:
        return redirect('index') 
    form = FormularioRegistro(request.POST or None)
    if request.method == 'POST' and form.is_valid():
      
        user = form.save()

        if user:
            messages.success(request, 'Usuario creado correctamente')
            return redirect('index')

    return render(request, 'usuarios/registro.html', {
        'form': form
    })

def inventario (request):

     return render (request, 'inventario/inventario.html' , {
        
    })