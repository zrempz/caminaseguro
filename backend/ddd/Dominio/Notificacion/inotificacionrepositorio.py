#-*- coding: utf-8 -*-

from Modelo.notificacion import Notificacion

class INotificacionRepositorio:

    def guardar_notificacion(self, notificacion: Notificacion):
        raise NotImplementedError("guardar_notificacion")

    def marcar_como_enviada(self, notificacion_id):
        raise NotImplementedError("marcar_como_enviada")