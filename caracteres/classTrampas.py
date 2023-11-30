import pygame as py
from caracteres.classObjetos import Object
from values.activos import *
from values.colores import *


class Trampas(Object):

    def __init__(self, tamano, posicion=(0, 0)) -> None:
        self.tamano = tamano

        super().__init__(tamano, posicion,r"imagenes\bombita.png")

    def actualizar(self,pantalla):
        """
        Brief:Actualiza la representación visual del objeto en la pantalla.
        Parametros: pantalla: La superficie de la pantalla en la que se va a actualizar el objeto.
        """
        self.blit(pantalla)
