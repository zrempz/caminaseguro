# DDD: Implementación del patrón Factory para la creación de la entidad Usuario.
# SOLID (SRP): La única responsabilidad de esta clase es crear instancias de Usuario.
from .modelo.usuario import Usuario
from ddd.infraestructura.servicios.servicio_hash import ServicioHash


class UsuarioFabrica:
    """
    Fábrica responsable de la creación de instancias de la entidad Usuario.

    Encapsula la lógica compleja de creación, como el hasheo de la contraseña,
    asegurando que los objetos se creen en un estado válido y consistente.
    Esto cumple con el patrón Factory de DDD.
    """

    def __init__(self, servicio_hash: ServicioHash):
        """
        Inicializa la fábrica con el servicio de hasheo.

        Args:
            servicio_hash (ServicioHash): El servicio para hashear contraseñas.
        """
        self._servicio_hash = servicio_hash

    def crear_usuario(self, nombre: str, email: str, password_plano: str) -> Usuario:
        """
        Crea una nueva instancia de Usuario, asegurando que la contraseña se hashee.

        Args:
            nombre (str): Nombre del usuario.
            email (str): Email del usuario.
            password_plano (str): Contraseña en texto plano.

        Returns:
            Usuario: Una nueva instancia de la entidad Usuario con la contraseña hasheada.
        """
        password_hasheado = self._servicio_hash.hash_password(password_plano)
        return Usuario(nombre=nombre, email=email, password=password_hasheado)
