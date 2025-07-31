#-*- coding: utf-8 -*-

from django.db import models
from ddd.dominio.usuarios.modelo.ubicacion import Ubicacion

class Registro(models.Model):
    class Meta:
        pass

    id = models.UUIDField()
    tipo_evento = models.CharField()
    fecha_hora = models.DateTimeField()
    ubicacion = Ubicacion()


    def es_evento_grave(self, ):
        pass

