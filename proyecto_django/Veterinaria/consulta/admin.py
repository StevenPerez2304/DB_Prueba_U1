from django.contrib import admin

# Register your models here.

from modelo.models import (
    Consulta,
    ConsultaPersonal
)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        'id_consulta',
        'id_mascota',
        'numero_consultas',
        'fecha',
    )

class ConsultaPersonalAdmin(admin.ModelAdmin):
    list_display = (
        'id_consulta',
        'codigo_personal',
    )

admin.site.register(Consulta)
#admin.site.register(ConsultaPersonal)
