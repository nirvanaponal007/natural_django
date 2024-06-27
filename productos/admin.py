from django.contrib import admin

# Registramos productos
from .models import Producto
admin.site.register(Producto)
