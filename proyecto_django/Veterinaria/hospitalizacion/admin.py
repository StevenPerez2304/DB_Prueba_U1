from django.contrib import admin

# Register your models here.

from modelo.models import (
    Personal,
    Veterinario,
    Auxiliar
)

class PersonalAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_personal',
        'cedula',
        'nombre',
    )

class VeterinarioAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_personal',
        'fecha_alta',
        'especialidad',
    )

class AuxiliarAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_personal',
        'cotizacion',
    )

admin.site.register(Personal)
admin.site.register(Veterinario)
admin.site.register(Auxiliar)