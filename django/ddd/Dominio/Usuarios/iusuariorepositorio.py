#-*- coding: utf-8 -*-

from django.db import models

class IUsuarioRepositorio(models.Model):
    class Meta:
        pass

    def guardar(self, usuario):
        pass

    def buscar_por_email(self, email):
        pass

    def eliminar_usuario(self, id):
        pass

