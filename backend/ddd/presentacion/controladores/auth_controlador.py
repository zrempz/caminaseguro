# ARQUITECTURA POR CAPAS: Esta capa solo maneja HTTP. Su responsabilidad es
# traducir las peticiones HTTP a llamadas a la capa de aplicación y
# transformar los resultados de vuelta a respuestas HTTP. No contiene lógica de negocio.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ddd.aplicacion.dto import CrearUsuarioDTO, LoginDTO
from ..contenedor import contenedor
from django.conf import settings
import jwt


class VistaRegistro(APIView):
    """
    Controlador de API (Endpoint) para el registro de nuevos usuarios.
    Maneja las peticiones POST a `/api/auth/registro/`.
    """

    def post(self, request):
        """
        Procesa la petición de registro.

        Args:
            request (Request): La petición HTTP entrante.

        Returns:
            Response: Una respuesta HTTP con los datos del usuario o un error.
        """
        try:
            dto = CrearUsuarioDTO(
                nombre=request.data.get("nombre", ""),
                email=request.data.get("email", ""),
                password=request.data.get("password", ""),
            )
        except TypeError:
            return Response(
                {"error": "Petición inválida."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            usuario_creado = contenedor.usuario_servicio.crear_usuario(dto)
            return Response(usuario_creado.__dict__, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            # CLEAN CODE: Captura genérica para errores no esperados.
            return Response(
                {"error": "Ocurrió un error inesperado."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class VistaLogin(APIView):
    """
    Controlador de API para el inicio de sesión de usuarios.
    Maneja las peticiones POST a `/api/auth/login/`.
    """

    def post(self, request):
        """
        Procesa la petición de inicio de sesión.

        Args:
            request (Request): La petición HTTP entrante.

        Returns:
            Response: Una respuesta HTTP con el token JWT o un error.
        """
        try:
            dto = LoginDTO(
                email=request.data.get("email", ""),
                password=request.data.get("password", ""),
            )
        except TypeError:
            return Response(
                {"error": "Petición inválida."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = contenedor.usuario_servicio.iniciar_sesion(dto)
            return Response(token.__dict__, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response(
                {"error": "Ocurrió un error inesperado."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class VistaUsuarioActual(APIView):
    """
    Endpoint protegido que devuelve los datos del usuario autenticado
    a partir del token JWT. Maneja las peticiones GET a `/api/auth/usuario/`.
    """

    def get(self, request):
        """
        Valida el token JWT y devuelve los datos del usuario.

        Args:
            request (Request): La petición HTTP entrante con el header 'Authorization'.

        Returns:
            Response: Una respuesta HTTP con los datos del usuario o un error.
        """
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return Response(
                {"error": "Token no proporcionado"}, status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            usuario = contenedor.usuario_repositorio.buscar_por_id(payload["id"])

            if not usuario:
                return Response(
                    {"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
                )

            return Response(usuario.a_diccionario())

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return Response(
                {"error": "Token inválido o expirado"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
