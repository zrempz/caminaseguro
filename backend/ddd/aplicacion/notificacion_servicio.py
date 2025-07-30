#-*- coding: utf-8 -*-

from django.db import models

class NotificacionServicio(models.Model):
    class Meta:
        abstract = True

    def enviar_notificacion(self, registro_id):
        pass

