from django.db import models
from django.contrib.auth.models import AbstractUser



# Proxy model >>  


class Cliente(AbstractUser):
    def obtener_full_nombre(self):
        return '{}{}'.format(self.first_name, self.last_name)
    
class Customer(Cliente):
    class Meta:
        proxy = True

    def obtener_producto(self):
        return[]


class Perfil(models.Model):
    usuario = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    biografia = models.TextField()