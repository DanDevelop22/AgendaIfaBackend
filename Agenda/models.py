from typing_extensions import Required
from django.db import models
from pkg_resources import require

# Create your models here.


class Oddun(models.Model):
    """Modelo para la informacion de cada oddun"""

    numero_oddun_bajada = models.IntegerField()
    numero_oddun_diloggun = models.CharField(blank=True)
    nombre = models.CharField(max_length=255)

    tradicional_ifa = models.TextField(blank=True)
    nace = models.TextField(blank=True)
    refranes = models.TextField(blank=True)

    tratado = models.TextField(blank=True)
    ebbo = models.TextField(blank=True)
    ewe = models.TextField(blank=True)
    ozain = models.TextField(blank=True)
    eshu = models.TextField(blank=True)
    patakies = models.TextField(blank=True)

    class Meta:
        ordering = ('numero_oddun_bajada',)

    def __str__(self):
        return self.nombre