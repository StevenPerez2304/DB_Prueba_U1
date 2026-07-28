# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    procesador = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=20, blank=True, null=True)
    almacenamiento = models.CharField(max_length=20, blank=True, null=True)
    tamano_pantalla = models.CharField(max_length=20, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    ruc = models.CharField(unique=True, max_length=15, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Suministro(models.Model):
    id_suministro = models.BigAutoField(primary_key=True)
    id_proveedor = models.IntegerField(blank=True, null=True)
    id_producto = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_suministro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suministro'
