from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productor(models.Model):
    nombres = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)
    correo = models.CharField(max_length=1000)
    direccion = models.CharField(max_length=1000)
    telefono = models.CharField(max_length=1000)
    latitud = models.FloatField()
    longitud = models.FloatField()
    extension = models.CharField(max_length=1000)
    usuarioId = models.OneToOneField(User)
