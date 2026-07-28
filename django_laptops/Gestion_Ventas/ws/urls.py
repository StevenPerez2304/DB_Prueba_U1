from django.urls import path

from .views import (
    ProductoListView,
    BuscarProductoView,
    ProveedorListView,
    BuscarProveedorView,
    SuministroListView,
    BuscarSuministroView,
)

urlpatterns = [
    # Productos
    path('productos/', ProductoListView.as_view(), name='productos'),
    path('buscar-producto/', BuscarProductoView.as_view(), name='buscar-producto'),

    # Proveedores
    path('proveedores/', ProveedorListView.as_view(), name='proveedores'),
    path('buscar-proveedor/', BuscarProveedorView.as_view(), name='buscar-proveedor'),

    # Suministros
    path('suministros/', SuministroListView.as_view(), name='suministros'),
    path('buscar-suministro/', BuscarSuministroView.as_view(), name='buscar-suministro'),
]