# CLEAN CODE: La clase representa un concepto único (Usuario) y sus atributos.
# DDD: Esta es nuestra Entidad principal en el subdominio de autenticación.
from mongoengine import Document, StringField, EmailField, UUIDField
from uuid import uuid4


class Usuario(Document):
    """
    Entidad de dominio que representa a un Usuario en el sistema.

    Esta clase es agnóstica a la persistencia y al framework, conteniendo solo
    los atributos y la estructura fundamental del usuario. Actúa como el 'Aggregate Root'
    para el agregado de Usuario.
    """

    id = UUIDField(primary_key=True, default=uuid4)
    nombre = StringField(required=True, max_length=150)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

    meta = {
        "collection": "usuarios",
        "indexes": ["email"],
    }

    def a_diccionario(self):
        """
        Convierte la entidad a un diccionario para transferencia de datos.

        Returns:
            dict: Un diccionario con los datos públicos del usuario.
        """
        return {
            "id": str(self.id),
            "nombre": str(self.nombre),
            "email": str(self.email),
        }
