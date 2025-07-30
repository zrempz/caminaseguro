#-*- coding: utf-8 -*-

from Modelo.notificacion import Notificacion

from django.db import models

class NotificacionFabrica(models.Model):
    @staticmethod
    def crear_notificacion(mensaje: str, fecha_hora: str) -> Notificacion:
        """Crea una nueva notificación con el mensaje y la fecha/hora proporcionados."""
        if not mensaje or not fecha_hora:
            raise ValueError("El mensaje y la fecha/hora son obligatorios.")
        return Notificacion(mensaje=mensaje)