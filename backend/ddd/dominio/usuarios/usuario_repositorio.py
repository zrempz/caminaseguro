#-*- coding: utf-8 -*-

from django.db import models

class UsuarioRepositorio(models.Model):
    class Meta:
        abstract = True

    def guardar(self, usuario):
        pass

    def eliminar(self, usuario_id):
        pass

    def buscar_por_id(self, usuario_id):
        pass

    def buscar_todos(self, ):
        pass

    def buscar_por_email(self, email):
        pass

