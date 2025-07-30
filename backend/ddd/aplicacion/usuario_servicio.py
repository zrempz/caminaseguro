from abc import ABC, abstractmethod
from .dto import CrearUsuarioDTO, UsuarioDTO, LoginDTO, TokenDTO


class UsuarioServicio(ABC):
    """
    Interfaz que define los casos de uso para la gestión de usuarios.
    """

    @abstractmethod
    def crear_usuario(self, crear_usuario_dto: CrearUsuarioDTO) -> UsuarioDTO:
        pass

    @abstractmethod
    def iniciar_sesion(self, login_dto: LoginDTO) -> TokenDTO:
        pass
