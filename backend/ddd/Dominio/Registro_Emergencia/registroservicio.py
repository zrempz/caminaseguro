## -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from .iregistrorepositorio import IRegistroRepositorio
from .registrofabrica import RegistroFabrica
from .Modelo.registro import Registro


class RegistroServicio:
    """
    Orquesta los casos de uso relacionados con los registros de emergencia.
    """

    def __init__(self, repositorio: IRegistroRepositorio):
        self._repositorio = repositorio
        self._fabrica = RegistroFabrica()

    def crear_registro(
        self, usuario_id: int, tipo_evento: str, descripcion: str, ubicacion: str
    ) -> Registro:
        """
        Crea un nuevo registro de emergencia de forma segura.

        Args:
            usuario_id (int): El ID del usuario que crea el reporte.
            tipo_evento (str): El tipo de evento (ej. "Robo", "Incendio").
            descripcion (str): Detalles adicionales del evento.
            ubicacion (str): Ubicación del evento.

        Returns:
            Registro: La entidad del registro creado.

        Raises:
            ValueError: Si el usuario_id proporcionado no existe.
        """
        try:
            usuario = User.objects.get(pk=usuario_id)
        except User.DoesNotExist:
            raise ValueError(
                f"No se puede crear el registro. Usuario no encontrado con ID: {usuario_id}"
            )

        registro = self._fabrica.crear_registro(
            usuario, tipo_evento, descripcion, ubicacion
        )
        self._repositorio.guardar_registro(registro)
        return registro
