from django.db import models

class Producto(models.Model):
    Nombre_Corto = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Precio_Venta = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombre_Corto
