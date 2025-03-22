import uuid
from django.db import models
from clientes.models import Cliente
from productos.models import Producto
from django.db.models.signals import pre_save



class Carro(models.Model):
    carro_id = models.CharField(max_length=100, null=False, blank= False , unique=True)
    usuario = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.carro_id

    
    

def set_carro_id(sender, instance, *args, **kwargs):
    if not instance.carro_id :
        instance.carro_id  = str(uuid.uuid4())
    
pre_save.connect(set_carro_id, sender=Carro)