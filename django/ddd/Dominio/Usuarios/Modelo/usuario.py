#-*- coding: utf-8 -*-

from django.db import models

class Usuario(models.Model):
    class Meta:
        pass

    id = models.UUIDField()
    nombre = models.CharField()
    telefono = models.CharField()
    email = models.CharField()


    def validar_email(self, ):
        pass

    def obtener_ubicacion(self, ):
        pass

