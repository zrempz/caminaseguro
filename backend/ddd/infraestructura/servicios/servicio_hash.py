from werkzeug.security import generate_password_hash, check_password_hash


class ServicioHash:
    """
    Proporciona una capa de abstracción para los servicios de hasheo de contraseñas.

    Utiliza algoritmos seguros que incluyen 'salting' para proteger las contraseñas,
    cumpliendo con las mejores prácticas de seguridad.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """Genera un hash seguro para una contraseña."""
        return generate_password_hash(password)

    @staticmethod
    def verificar_password(password_hash: str, password_plano: str) -> bool:
        """Verifica si una contraseña en texto plano coincide con su hash."""
        return check_password_hash(password_hash, password_plano)
