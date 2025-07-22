# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.contrib.auth.models import User  # Asumiendo que usas el User de Django


class Registro(models.Model):
    """
    Representa una emergencia reportada en el sistema.

    Encapsula todos los datos y la lógica de negocio directamente
    relacionada con un registro, como determinar su gravedad.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True, editable=False)
    es_grave = models.BooleanField(default=False)

    def _marcar_como_grave(self):
        """Lógica de negocio interna para determinar la gravedad."""
        eventos_graves = ["incendio", "asalto con arma", "accidente vehicular mayor"]
        if self.tipo_evento.lower() in eventos_graves:
            self.es_grave = True
        else:
            self.es_grave = False

    def save(self, *args, **kwargs):
        """Asegura que la lógica de negocio se ejecute antes de guardar."""
        self._marcar_como_grave()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Registro de Emergencia"
        ordering = ["-fecha_hora"]
