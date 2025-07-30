#-*- coding: utf-8 -*-

from django.db import models
import uuid

class ContactoEmergencia(models.Model):
    """
    Modelo de dominio para un Contacto de Emergencia.
    Representa una persona a la que se puede alertar en caso de emergencia.
    """
    class Meta:
        verbose_name = "Contacto de Emergencia"
        verbose_name_plural = "Contactos de Emergencia"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    relacion = models.CharField(max_length=50)

    def __str__(self):
        """
        Representación en cadena del contacto.
        """
        return f"{self.nombre} ({self.relacion})"
