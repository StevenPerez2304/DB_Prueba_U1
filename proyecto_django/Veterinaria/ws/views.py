from django.shortcuts import render, redirect
from modelo.models import Consulta, Mascota
from.serializers import ConsultaSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView )
from rest_framework.generics import ListAPIView
from modelo.models import Consulta
from .serializers import ConsultaSerializer
from django.http import JsonResponse
import requests

# Create your views here.
class ConsultaListView(ListAPIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        queryset = Consulta.objects.all()

        id_mascota = self.request.GET.get('id_mascota')

        if id_mascota:
            queryset = queryset.filter(id_mascota=id_mascota)

        return queryset


def guardar_consultas(request):

    mascotas = Mascota.objects.all()
    veterinarios = []

    response = requests.get(
        'http://localhost:8001/ws/veterinarios'
    )

    if response.status_code == 200:
        veterinarios = response.json()

    if request.method == 'POST':

        mascota = Mascota.objects.get(
            id=request.POST['id_mascota']
        )

        ultima = Consulta.objects.order_by(
            '-id_consulta'
        ).first()

        if ultima:
            numero = int(ultima.id_consulta[1:]) + 1
        else:
            numero = 1

        nuevo_id = f"C{numero:03d}"

        consulta = Consulta(
            id_consulta=nuevo_id,
            id_mascota=mascota,
            numero_consultas=request.POST['numero_consultas'],
            diagnostico=request.POST['diagnostico'],
            fecha=request.POST['fecha']
        )

        consulta.save()

        return redirect('/consulta/guardar-consulta/')

    return render(
        request,
        'guardar_consultas.html',
        {
            'mascotas': mascotas,
            'veterinarios': veterinarios
        }
    )
