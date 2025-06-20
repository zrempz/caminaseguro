#-*- coding: utf-8 -*-

from django.db import models

class INotificacionRepositorio(models.Model):
    class Meta:
        pass

    def guardar_notificacion(self, notificacion):
        pass

    def marcar_como_enviada(self, notificacion_id):
        pass

