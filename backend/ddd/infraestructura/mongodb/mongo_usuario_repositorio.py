# DDD: Implementación concreta del Repositorio de Usuarios.
# ARQUITECTURA: Reside en la infraestructura porque depende de una tecnología
# de base de datos específica (MongoEngine para MongoDB).

from ddd.dominio.usuarios.usuario_repositorio import UsuarioRepositorio
from ddd.dominio.usuarios.modelo.usuario import Usuario


class MongoUsuarioRepositorio(UsuarioRepositorio):
    """
    Implementación del Repositorio de Usuarios que utiliza MongoDB como
    mecanismo de persistencia a través de la librería MongoEngine.
    """

    def guardar(self, usuario: Usuario) -> Usuario:
        """
        Guarda o actualiza un documento de usuario en MongoDB.

        Args:
            usuario (Usuario): La entidad de usuario a persistir.

        Returns:
            Usuario: La entidad de usuario guardada.
        """
        usuario.save()  # Método de MongoEngine para guardar o actualizar
        return usuario

    def buscar_por_email(self, email: str) -> Usuario | None:
        """
        Busca un usuario por su email en la colección de usuarios.

        Args:
            email (str): El email a buscar.

        Returns:
            Usuario | None: La entidad de usuario si se encuentra, o None.
        """
        return Usuario.objects(email=email).first()

    def existe_email(self, email: str) -> bool:
        """
        Verifica la existencia de un usuario por su email.

        Args:
            email (str): El email a verificar.

        Returns:
            bool: True si el email existe, False en caso contrario.
        """
        return Usuario.objects(email=email).count() > 0

    def buscar_por_id(self, usuario_id: str) -> Usuario | None:
        """
        Busca un usuario por su ID en MongoDB.

        Args:
            usuario_id (str): El ID del usuario a buscar.

        Returns:
            Usuario | None: El objeto de usuario si se encuentra, o None.
        """
        return Usuario.objects(id=usuario_id).first()
