#-*- coding: utf-8 -*-

from django.db import models

class Notificacion(models.Model):
    class Meta:
        pass

    id = models.UUIDField()
    mensaje = models.CharField()
    fecha_hora = models.DateTimeField()
    enviado = models.BooleanField()


