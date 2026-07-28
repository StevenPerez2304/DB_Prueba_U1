from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Producto, Proveedor, Suministro
from .serializers import (
    ProductoSerializer,
    ProveedorSerializer,
    SuministroSerializer
)


class ProductoListView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()

        marca = self.request.GET.get('marca')

        if marca:
            queryset = queryset.filter(marca__icontains=marca)

        return queryset


class BuscarProductoView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()

        id_producto = self.request.GET.get('id_producto')
        modelo = self.request.GET.get('modelo')
        procesador = self.request.GET.get('procesador')

        if id_producto:
            queryset = queryset.filter(id_producto=id_producto)

        if modelo:
            queryset = queryset.filter(modelo__icontains=modelo)

        if procesador:
            queryset = queryset.filter(procesador__icontains=procesador)

        return queryset


class ProveedorListView(ListAPIView):
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        queryset = Proveedor.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            queryset = queryset.filter(nombre_empresa__icontains=nombre)

        return queryset


class BuscarProveedorView(ListAPIView):
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        queryset = Proveedor.objects.all()

        ruc = self.request.GET.get('ruc')
        empresa = self.request.GET.get('empresa')

        if ruc:
            queryset = queryset.filter(ruc__icontains=ruc)

        if empresa:
            queryset = queryset.filter(nombre_empresa__icontains=empresa)

        return queryset


class SuministroListView(ListAPIView):
    serializer_class = SuministroSerializer

    def get_queryset(self):
        queryset = Suministro.objects.all()

        fecha = self.request.GET.get('fecha')

        if fecha:
            queryset = queryset.filter(fecha_suministro=fecha)

        return queryset


class BuscarSuministroView(ListAPIView):
    serializer_class = SuministroSerializer

    def get_queryset(self):
        queryset = Suministro.objects.all()

        id_producto = self.request.GET.get('id_producto')
        id_proveedor = self.request.GET.get('id_proveedor')

        if id_producto:
            queryset = queryset.filter(id_producto=id_producto)

        if id_proveedor:
            queryset = queryset.filter(id_proveedor=id_proveedor)

        return queryset

# Create your views here.
