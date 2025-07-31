from abc import ABC, abstractmethod
from .modelo.usuario import Usuario


class UsuarioRepositorio(ABC):
    """
    Interfaz que define las operaciones de persistencia para la entidad Usuario.

    Actúa como un contrato que la capa de infraestructura debe implementar,
    desacoplando el dominio de los detalles de la base de datos.
    """

    @abstractmethod
    def guardar(self, usuario: Usuario) -> Usuario:
        """Guarda o actualiza una entidad de Usuario en el repositorio."""
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario | None:
        """Busca un usuario por su dirección de email."""
        pass

    @abstractmethod
    def existe_email(self, email: str) -> bool:
        """Verifica si ya existe un usuario con un email determinado."""
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_id: str) -> Usuario | None:
        """Busca un usuario por su ID único."""
        pass
