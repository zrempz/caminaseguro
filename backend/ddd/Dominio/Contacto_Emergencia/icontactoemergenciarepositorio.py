#-*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List, Optional
import uuid 
from ddd.Dominio.Contacto_Emergencia.Modelo.contactoemergencia import ContactoEmergencia

class IContactoEmergenciaRepositorio(ABC):
    """
    Interfaz abstracta para el repositorio de ContactoEmergencia.
    Define los métodos que cualquier implementación de repositorio debe proveer.
    """
    @abstractmethod
    def guardar_contacto(self, contacto: ContactoEmergencia) -> ContactoEmergencia:
        """
        Guarda o actualiza una instancia de ContactoEmergencia en el almacenamiento.
        """
        pass

    @abstractmethod
    def obtener_contactos(self) -> List[ContactoEmergencia]:
        """
        Obtiene una lista de todos los contactos de emergencia.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, contacto_id: uuid.UUID) -> Optional[ContactoEmergencia]:
        """
        Busca un contacto por su ID. Retorna el contacto o None si no se encuentra.
        """
        pass

    @abstractmethod
    def eliminar_contacto(self, contacto: ContactoEmergencia):
        """
        Elimina un contacto del almacenamiento.
        """
        pass
