#-*- coding: utf-8 -*-

from django.db import models
import uuid

class Notificacion(models.Model):
    "Modelo de Notificación que representa una notificación en el sistema."
    id = models.UUIDField()
    mensaje = models.CharField()
    fecha_hora = models.DateTimeField()
    enviado = models.BooleanField()
    
    def marcar_como_enviada(self):
        self.enviado = True
        self.save()