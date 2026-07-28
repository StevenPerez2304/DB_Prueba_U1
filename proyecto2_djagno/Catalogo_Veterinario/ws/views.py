from django.shortcuts import render
from .models import Veterinario, VeterinarioEspecialidad, Especialidad
from .serializers import VeterinarioSerializer , EspecialidadSerializer , VeterinarioEspecialidadSerializer
# Create your views here.

from rest_framework.generics import (ListAPIView, RetrieveAPIView)

class VeterinarioListView(ListAPIView):
    serializer_class = VeterinarioSerializer

    def get_queryset(self):
        queryset = Veterinario.objects.filter(activo=True)
        nombre = self.request.GET.get('nombre')

        if nombre:
            queryset = queryset.filter(nombres__icontains=nombre)

        return queryset

class BuscarVeterinarioView(ListAPIView):
    serializer_class = VeterinarioSerializer

    def get_queryset(self):
        queryset = Veterinario.objects.filter(activo=1)
        cedula = self.request.GET.get('cedula')
        apellidos = self.request.GET.get('apellidos')

        if cedula:
            queryset = queryset.filter(cedula__icontains=cedula)
        if apellidos:
            queryset = queryset.filter(apellidos__icontains=apellidos)

        return queryset

class BuscarVeterinarioEspecialidadView(ListAPIView):
    serializer_class = VeterinarioEspecialidadSerializer

    def get_queryset(self):
        queryset = VeterinarioEspecialidad.objects.all()

        especialidad = self.request.GET.get('especialidad')

        if especialidad:
            queryset = queryset.filter(
                id_especialidad__nombre__icontains=especialidad
            )

        return queryset

class BuscarEspecialidadView(ListAPIView):
    serializer_class = EspecialidadSerializer

    def get_queryset(self):
        queryset = Especialidad.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            queryset = queryset.filter(
                nombre__icontains=nombre
            )

        return queryset