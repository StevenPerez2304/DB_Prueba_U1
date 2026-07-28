from rest_framework import serializers
from .models import Veterinario, Especialidad, VeterinarioEspecialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class VeterinarioSerializer(serializers.ModelSerializer):
    especialidades = serializers.SerializerMethodField()

    class Meta:
        model = Veterinario
        fields = '__all__'

    def get_especialidades(self, obj):
        relaciones = VeterinarioEspecialidad.objects.filter(id_veterinario=obj)
        return [r.id_especialidad.nombre for r in relaciones]


class VeterinarioEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinarioEspecialidad
        fields = '__all__'

