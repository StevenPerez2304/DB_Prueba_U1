from django.contrib import admin

# Register your models here.
from modelo.models import  PropietarioMascota, Mascota, ContactoEmergencia

class PropietarioAdmin(admin.ModelAdmin):
    list_display = (
        'CI',
        'nombres',
        'apellidos',
        'direccion',
        'telefono',
    )

class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'CI_propietario',
        'nombre',
        'fecha_nacimiento',
        'raza',
    )

class ContactoEmergenciaAdmin(admin.ModelAdmin):
    list_display = (
        'ci_contacto',
        'ci_propietario_m',
        'nombre',
        'telefono',
    )


admin.site.register(PropietarioMascota)
admin.site.register(Mascota)
#admin.site.register(ContactoEmergencia)

