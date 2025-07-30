#-*- coding: utf-8 -*-

from ddd.Dominio.Contacto_Emergencia.Modelo.contactoemergencia import ContactoEmergencia

class ContactoEmergenciaFabrica:
    """
    Fábrica para crear instancias de ContactoEmergencia.
    """
    def crear_contacto(self, nombre: str, telefono: str, relacion: str) -> ContactoEmergencia:
        """
        Crea una nueva instancia de ContactoEmergencia en memoria.
        """
        contacto = ContactoEmergencia(
            nombre=nombre,
            telefono=telefono,
            relacion=relacion
        )
        return contacto
