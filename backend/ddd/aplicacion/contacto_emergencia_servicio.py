#-*- coding: utf-8 -*-

from django.db import models

class ContactoEmergenciaServicio(models.Model):
    class Meta:
        abstract = True

    def agregar_contacto(self, contacto):
        pass

    def obtener_contactos(self, ):
        pass

