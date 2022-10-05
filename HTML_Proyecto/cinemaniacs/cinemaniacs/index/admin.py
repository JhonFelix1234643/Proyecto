from django.contrib import admin
from .models import Genero, Pelicula, PeliculaHasGenero, Usuariocine

# Register your models here.
admin.site.register(Usuariocine)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(PeliculaHasGenero)