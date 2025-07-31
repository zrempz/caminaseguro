from django.urls import path
from .controladores.auth_controlador import (
    VistaRegistro,
    VistaLogin,
    VistaUsuarioActual,
)

urlpatterns = [
    path("auth/registro/", VistaRegistro.as_view(), name="registro"),
    path("auth/login/", VistaLogin.as_view(), name="login"),
    path("auth/usuario/", VistaUsuarioActual.as_view(), name="usuario-actual"),
]
