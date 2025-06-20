#-*- coding: utf-8 -*-

from django.db import models

class ContactoEmergencia(models.Model):
    class Meta:
        pass

    id = models.UUIDField()
    nombre = models.CharField()
    telefono = models.CharField()
    relacion = models.CharField()


