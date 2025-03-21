from .models import Cliente
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Cliente, UserAdmin)
