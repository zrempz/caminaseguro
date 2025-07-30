#-*- coding: utf-8 -*-

from django.db import models

class Registro(models.Model):
    class Meta:
        pass

    id = models.UUIDField()
    tipo_evento = models.CharField()
    fecha_hora = models.DateTimeField()
    ubicacion = undefined()


    def es_evento_grave(self, ):
        pass

