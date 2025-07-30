# SOLID (DIP): El servicio recibe sus dependencias (repositorio, fábrica) en el
# constructor, en lugar de crearlas internamente (Inyección de Dependencias).
# CLEAN CODE: Las funciones orquestan un único caso de uso.

from .usuario_servicio import UsuarioServicio
from .dto import CrearUsuarioDTO, UsuarioDTO, LoginDTO, TokenDTO
from ddd.dominio.usuarios.usuario_repositorio import UsuarioRepositorio
from ddd.dominio.usuarios.usuario_fabrica import UsuarioFabrica
from ddd.infraestructura.servicios.servicio_hash import ServicioHash
from django.conf import settings
import jwt
import datetime


class UsuarioServicioImpl(UsuarioServicio):
    """
    Implementación de los casos de uso relacionados con la autenticación de usuarios.

    Orquesta las interacciones entre las entidades del dominio, los repositorios
    y otros servicios para cumplir con las reglas de negocio, siguiendo los
    principios de la Arquitectura Limpia.
    """

    def __init__(
        self,
        usuario_repositorio: UsuarioRepositorio,
        usuario_fabrica: UsuarioFabrica,
        servicio_hash: ServicioHash,
    ):
        """
        Inicializa el servicio con sus dependencias.

        Args:
            usuario_repositorio (UsuarioRepositorio): El repositorio para la persistencia de usuarios.
            usuario_fabrica (UsuarioFabrica): La fábrica para crear entidades de usuario.
            servicio_hash (ServicioHash): El servicio para el hasheo de contraseñas.
        """
        self.usuario_repositorio = usuario_repositorio
        self.usuario_fabrica = usuario_fabrica
        self.servicio_hash = servicio_hash

    def crear_usuario(self, crear_usuario_dto: CrearUsuarioDTO) -> UsuarioDTO:
        """
        Orquesta la creación de un nuevo usuario.

        Args:
            crear_usuario_dto (CrearUsuarioDTO): DTO con la información del nuevo usuario.

        Returns:
            UsuarioDTO: DTO con los datos del usuario recién creado.

        Raises:
            ValueError: Si el email ya se encuentra registrado.
        """
        if self.usuario_repositorio.existe_email(crear_usuario_dto.email):
            raise ValueError("El email ya está en uso.")

        nuevo_usuario = self.usuario_fabrica.crear_usuario(
            nombre=crear_usuario_dto.nombre,
            email=crear_usuario_dto.email,
            password_plano=crear_usuario_dto.password,
        )

        usuario_guardado = self.usuario_repositorio.guardar(nuevo_usuario)

        return UsuarioDTO(
            id=str(usuario_guardado.id),
            nombre=str(usuario_guardado.nombre),
            email=str(usuario_guardado.email),
        )

    def iniciar_sesion(self, login_dto: LoginDTO) -> TokenDTO:
        """
        Orquesta el proceso de inicio de sesión.

        Args:
            login_dto (LoginDTO): DTO con las credenciales del usuario.

        Returns:
            TokenDTO: DTO que contiene el token JWT para la sesión.

        Raises:
            ValueError: Si las credenciales son inválidas.
        """
        usuario = self.usuario_repositorio.buscar_por_email(login_dto.email)

        if not usuario or not self.servicio_hash.verificar_password(
            str(usuario.password), login_dto.password
        ):
            raise ValueError("Las credenciales proporcionadas son inválidas.")

        payload = {
            "id": str(usuario.id),
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(hours=24),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return TokenDTO(token=token)
