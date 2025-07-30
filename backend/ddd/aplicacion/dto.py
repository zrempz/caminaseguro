# CLEAN CODE: dataclasses para crear objetos inmutables de transferencia
# de datos. Esto es preferible a usar diccionarios, ya que provee tipado estático
# y mejora la legibilidad y seguridad del código.
from dataclasses import dataclass


@dataclass(frozen=True)
class CrearUsuarioDTO:
    """
    DTO para transportar los datos necesarios para crear un usuario.

    Atributos:
        nombre (str): El nombre completo del usuario.
        email (str): La dirección de correo electrónico del usuario.
        password (str): La contraseña en texto plano.
    """

    nombre: str
    email: str
    password: str


@dataclass(frozen=True)
class UsuarioDTO:
    """
    DTO para exponer los datos de un usuario de forma segura, sin incluir
    información sensible como la contraseña.

    Atributos:
        id (str): El identificador único del usuario.
        nombre (str): El nombre completo del usuario.
        email (str): La dirección de correo electrónico del usuario.
    """

    id: str
    nombre: str
    email: str


@dataclass(frozen=True)
class LoginDTO:
    """
    DTO para transportar las credenciales de inicio de sesión.

    Atributos:
        email (str): El email proporcionado por el usuario.
        password (str): La contraseña en texto plano proporcionada.
    """

    email: str
    password: str


@dataclass(frozen=True)
class TokenDTO:
    """
    DTO para devolver el token de autenticación JWT.

    Atributos:
        token (str): El JSON Web Token generado para la sesión del usuario.
    """

    token: str
