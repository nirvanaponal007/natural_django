from django.contrib import admin
from .models import Carro






class CarroAdmin(admin.ModelAdmin):
    fields = ('carro_id','usuario','productos','subtotal','total')
    list_display = ('usuario','id')



admin.site.register(Carro, CarroAdmin)
# Register your models here.
