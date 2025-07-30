#-*- coding: utf-8 -*-

from django.db import models

class RegistroEmergenciaServicio(models.Model):
    class Meta:
        abstract = True

    def obtener_registros_graves(self, ):
        pass

    def guardar_registro(self, registro):
        pass

