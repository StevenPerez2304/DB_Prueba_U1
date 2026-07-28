from django.urls import path
from .views import VentaListView, registrar_venta

urlpatterns = [
    path('ventas/', VentaListView.as_view(), name='ventas'),
    path('registrar-venta/', registrar_venta, name='registrar_venta'),
]