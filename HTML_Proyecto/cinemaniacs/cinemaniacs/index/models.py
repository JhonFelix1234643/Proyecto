# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Genero(models.Model):
    id_genero = models.IntegerField(db_column='ID_Genero', primary_key=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'genero'


class Pelicula(models.Model):
    id_pelicula = models.IntegerField(db_column='ID_Pelicula', primary_key=True)  # Field name made lowercase.
    nombre_pelicula = models.CharField(db_column='Nombre_Pelicula', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=45)  # Field name made lowercase.
    duracion = models.CharField(db_column='Duracion', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'pelicula'


class PeliculaHasGenero(models.Model):
    pelicula_id_pelicula = models.OneToOneField(Pelicula, models.DO_NOTHING, db_column='Pelicula_ID_Pelicula', primary_key=True)  # Field name made lowercase.
    genero_id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='Genero_ID_Genero')  # Field name made lowercase.

    class Meta:
        db_table = 'pelicula_has_genero'
        unique_together = (('pelicula_id_pelicula', 'genero_id_genero'),)


class Usuario(models.Model):
    id_usuario = models.IntegerField(db_column='ID_Usuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=50)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=45)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'usuario'
