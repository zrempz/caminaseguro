#-*- coding: utf-8 -*-

from Modelo.notificacion import Notificacion
from ..inotificacionrepositorio import INotificacionRepositorio

class NotificacionServicioDominio:
    def __init__(self, repositorio: INotificacionRepositorio):
        self.repositorio = repositorio

    def enviar_notificacion(self, mensaje: str, destinatario: str):
        notificacion = Notificacion(mensaje=mensaje, destinatario=destinatario)
        self.repositorio.guardar_notificacion(notificacion)
        notificacion.marcar_como_enviada()
        self.repositorio.marcar_como_enviada(notificacion.id)