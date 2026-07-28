# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Auxiliar(models.Model):
    codigo_personal = models.OneToOneField('Personal', models.DO_NOTHING, db_column='codigo_personal', primary_key=True)
    cotizacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'auxiliar'

class Consulta(models.Model):
    id_consulta = models.CharField(primary_key=True, max_length=10)
    id_mascota = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='id_mascota', blank=True, null=True)
    numero_consultas = models.IntegerField()
    diagnostico = models.TextField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'consulta'

class ConsultaPersonal(models.Model):
    pk = models.CompositePrimaryKey('id_consulta', 'codigo_personal')
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta')
    codigo_personal = models.ForeignKey('Personal', models.DO_NOTHING, db_column='codigo_personal')

    class Meta:
        managed = False
        db_table = 'consulta_personal'

class ContactoEmergencia(models.Model):
    pk = models.CompositePrimaryKey('ci_contacto', 'ci_propietario_m')
    ci_contacto = models.CharField(db_column='CI_contacto', max_length=10)  # Field name made lowercase.
    ci_propietario_m = models.ForeignKey('PropietarioMascota', models.DO_NOTHING, db_column='CI_propietario_m')  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'contacto_emergencia'

class Mascota(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    ci_propietario = models.ForeignKey('PropietarioMascota', models.DO_NOTHING, db_column='CI_propietario', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mascota'


class Personal(models.Model):
    codigo_personal = models.CharField(primary_key=True, max_length=10)
    cedula = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'personal'


class PropietarioMascota(models.Model):
    ci = models.CharField(db_column='CI', primary_key=True, max_length=15)  # Field name made lowercase.
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'propietario_mascota'


class Veterinario(models.Model):
    codigo_personal = models.OneToOneField(Personal, models.DO_NOTHING, db_column='codigo_personal', primary_key=True)
    fecha_alta = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'veterinario'
