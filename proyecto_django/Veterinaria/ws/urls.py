from django.urls import path

from .views import (ConsultaListView , guardar_consultas)

urlpatterns = [
    path('Consulta/', ConsultaListView.as_view()),
    path('guardar-consulta/', guardar_consultas, name='guardar_consultas'),
]