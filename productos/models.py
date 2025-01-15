from django.db import models
from django.utils.text import slugify

class Producto(models.Model):
    Nombre_Corto = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Precio_Venta = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Nombre_Corto)
        super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return self.Nombre_Corto
