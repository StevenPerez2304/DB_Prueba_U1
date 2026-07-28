# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    anios_experiencia = models.IntegerField(blank=True, null=True)
    universidad = models.CharField(max_length=150, blank=True, null=True)
    numero_registro = models.CharField(unique=True, max_length=50)
    foto = models.CharField(max_length=255, blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinario'


class VeterinarioEspecialidad(models.Model):
    id_veterinario_especialidad = models.AutoField(primary_key=True)
    id_veterinario = models.ForeignKey(Veterinario, models.DO_NOTHING, db_column='id_veterinario', blank=True, null=True)
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinario_especialidad'
