from django.db import models
from datetime import datetime
# Create your models here.


#ID_Usuario,Nombre,Apellido,Telefono,Correo,Rol,Contraseña
class User(models.Model):
    id_user = models.AutoField('Id',primary_key=True)
    name = models.CharField('Nombres completos', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    phone = models.CharField('Telefono', max_length=50)
    e_mail = models.CharField('Correo', max_length=150)

    def __str__(self):
        return self.id_user

    class Meta:
        verbose_name='Id usuario'
        verbose_name_plural='Id usuarios'
        db_table= 'User'
        ordering=['id_user']

# Tabla Pelicula-------------------------------------------------------------------------
class Movie(models.Model):
    id_movie = models.AutoField('Id Película',primary_key=True)
    name_movie = models.CharField('Nombre Película', max_length=250)
    description = models.TextField('Descripción')
    director = models.CharField('Director', max_length=60)
    last = models.CharField('Duración',max_length=15)

    def __str__(self):
        return self.id_movie

    class Meta:
        verbose_name='Id Película'
        verbose_name_plural='Id Películas'
        db_table= 'movie'
        ordering=['id_movie']

# Tabla Genero--------------------------------------------------------------------------
# ID_Genero,Genero
class Genres(models.Model):
    id_genres = models.AutoField('Id Genero',primary_key=True)
    name_genres = models.CharField('Genero', max_length=250)

    def __str__(self):
        return self.id_genres

    class Meta:
        verbose_name='Id Genero'
        verbose_name_plural='Id Generos'
        db_table= 'genres'
        ordering=['id_genres']

#Tabla pelicula_has_genero----------------------------------------------------------------
#(Pelicula_ID_Pelicula,Genero_ID_Genero)
class Movie_has_genre(models.Model):
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    id_genres = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_movie

    class Meta:
        verbose_name='Id Película'
        verbose_name_plural='Id Películas'
        db_table= 'movie'
        ordering=['id_movie']