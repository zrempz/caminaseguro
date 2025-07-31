#-*- coding: utf-8 -*-

from django.db import models

class NotificacionRepositorio(models.Model):
    class Meta:
        abstract = True

    def guardar(self, notificacion):
        pass

    def eliminar(self, notificacion_id):
        pass

    def buscar_por_id(self, notificacion_id):
        pass

    def buscar_todos(self, ):
        pass

