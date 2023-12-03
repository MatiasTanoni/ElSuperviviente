from Modulos.Niveles.nivel_uno import *
from Modulos.Niveles.classNivelDos import *
from Modulos.Niveles.classNivelTres import *


class ManejadorDeNiveles:
    def __init__(self) -> None:
        """
        Brief: Constructor de la clase DriverLevels.

        Descripción:
            Inicializa un objeto DriverLevels con un diccionario que asocia nombres de niveles con las clases
            correspondientes de esos niveles.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.niveles = {"level_one": NivelUno, "level_two": NivelDos, "level_three": NivelTres}

    def get_level(self, name_level):
        """
        Brief: Obtiene una instancia de un nivel específico.

        Descripción:
            Este método devuelve una instancia de la clase correspondiente al nivel especificado.

        Parámetros:
            - name_level (str): Nombre del nivel para el cual se desea obtener una instancia.

        Retorno:
            object: Instancia de la clase del nivel especificado.
        """
        return self.niveles[name_level]((1200, 650))