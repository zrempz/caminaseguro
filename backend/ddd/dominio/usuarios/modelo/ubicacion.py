#-*- coding: utf-8 -*-

from django.db import models

class Ubicacion(models.Model):
    class Meta:
        pass

    latitud = models.DecimalField()
    longitud = models.DecimalField()
    referencia = models.CharField()


    def esta_dentro_radio(self, lat, lon, radio_km):
        pass

