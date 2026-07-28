from django.urls import path

from .views import (VeterinarioListView, BuscarVeterinarioView, BuscarVeterinarioEspecialidadView, BuscarEspecialidadView)

urlpatterns = [
    path('veterinarios/', VeterinarioListView.as_view(),name='veterinarios'),
    path('buscarcedula/', BuscarVeterinarioView.as_view()),
    path('buscar-veterinario-especialidad/', BuscarVeterinarioEspecialidadView.as_view()),
    path('buscar-especialidad/', BuscarEspecialidadView.as_view()),
]