# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula_cliente = models.CharField(unique=True, max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Credencial(models.Model):
    id_credencial = models.AutoField(primary_key=True)
    id_empleado = models.OneToOneField('Empleado', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    contrasena = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credencial'


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_venta'



class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    cedula_empleado = models.CharField(unique=True, max_length=15)
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    apellido_completo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_venta', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
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
    id_proveedor = models.AutoField(primary_key=True)
    ruc = models.CharField(unique=True, max_length=15, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Suministro(models.Model):
    id_suministro = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_suministro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suministro'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
