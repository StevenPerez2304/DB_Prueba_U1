import requests
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView

from modelo.models import Venta, DetalleVenta, Cliente, Empleado
from .serializers import VentaSerializer


class VentaListView(ListAPIView):
    serializer_class = VentaSerializer

    def get_queryset(self):
        return Venta.objects.all()


def registrar_venta(request):

    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()

    # ==========================
    # PRODUCTOS DESDE WEB SERVICE
    # ==========================
    productos = []
    try:
        respuesta = requests.get("http://localhost:8001/ws/productos/")
        if respuesta.status_code == 200:
            productos = respuesta.json()
    except:
        pass

    # ==========================
    # PROVEEDORES DESDE WEB SERVICE
    # ==========================
    proveedores = []
    try:
        respuesta = requests.get("http://localhost:8001/ws/proveedores/")
        if respuesta.status_code == 200:
            proveedores = respuesta.json()
    except:
        pass

    if request.method == "POST":

        cliente = Cliente.objects.get(
            id_cliente=request.POST["id_cliente"]
        )

        empleado = Empleado.objects.get(
            id_empleado=request.POST["id_empleado"]
        )

        venta = Venta.objects.create(
            id_cliente=cliente,
            id_empleado=empleado,
            fecha=request.POST["fecha"]
        )

        cantidad = int(request.POST["cantidad"])
        precio = float(request.POST["precio_unitario"])

        DetalleVenta.objects.create(
            id_venta=venta,
            id_producto_id=request.POST["id_producto"],
            cantidad=cantidad,
            precio_unitario=precio,
            total=cantidad * precio
        )

        return redirect("registrar_venta")

    return render(
        request,
        "registrar_venta.html",
        {
            "clientes": clientes,
            "empleados": empleados,
            "productos": productos,
            "proveedores": proveedores
        }
    )