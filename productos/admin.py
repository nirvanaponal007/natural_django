from django.contrib import admin

# Registramos productos
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    fields = ('Nombre_Corto','Descripcion','Precio_Venta')
    list_display = ('__str__','slug','created_at')


admin.site.register(Producto , ProductoAdmin) 



