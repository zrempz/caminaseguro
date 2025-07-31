#-*- coding: utf-8 -*-

from django.db import models

class RegistroRepositorio(models.Model):
    class Meta:
        abstract = True

    def guardar(self, registro):
        pass

    def eliminar(self, registro_id):
        pass

    def buscar_por_id(self, registro_id):
        pass

    def buscar_todos(self, ):
        pass

