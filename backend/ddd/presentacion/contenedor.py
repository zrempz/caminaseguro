# SOLID (DIP): Este es un contenedor simple para la Inyección de Dependencias.
# Centraliza la creación y el "cableado" de las clases de servicio,
# repositorio y fábrica, facilitando la gestión de dependencias.
from ddd.infraestructura.mongodb.mongo_usuario_repositorio import (
    MongoUsuarioRepositorio,
)
from ddd.infraestructura.servicios.servicio_hash import ServicioHash
from ddd.dominio.usuarios.usuario_fabrica import UsuarioFabrica
from ddd.aplicacion.usuario_servicio_impl import UsuarioServicioImpl


class Contenedor:
    """
    Contenedor para la gestión de inyección de dependencias.
    """

    def __init__(self):
        # Infraestructura
        self.servicio_hash = ServicioHash()
        self.usuario_repositorio = MongoUsuarioRepositorio()

        # Dominio (Fábricas)
        self.usuario_fabrica = UsuarioFabrica(servicio_hash=self.servicio_hash)

        # Aplicación
        self.usuario_servicio = UsuarioServicioImpl(
            usuario_repositorio=self.usuario_repositorio,
            usuario_fabrica=self.usuario_fabrica,
            servicio_hash=self.servicio_hash,
        )


# Se crea una instancia única (Singleton) del contenedor para toda la aplicación.
contenedor = Contenedor()
