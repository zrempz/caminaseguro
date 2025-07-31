#-*- coding: utf-8 -*-

from django.db import models

class ContactoEmergenciaRepositorio(models.Model):
    class Meta:
        abstract = True

    def guardar(self, contacto):
        pass

    def eliminar(self, contacto_id):
        pass

    def buscar_por_id(self, contacto_id):
        pass

    def buscar_todos(self, ):
        pass

