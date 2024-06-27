from django.urls import path
from . import views

#llave utilizada

urlpatterns = [
    path('<pk>', views.ProductoDetalleView.as_view(), name='producto')
]