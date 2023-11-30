import pygame as py
from caracteres.classObjetos import Object
from values.activos import *
from values.colores import *


class Item(Object):

    def __init__(self, tamano, tipo="", posicion=(0, 0)) -> None:
        self.tamano = tamano
        self.tipo = tipo
        if tipo == "agua":
            super().__init__(tamano, posicion,r"imagenes\agua.png")
        elif tipo == "comida":
            super().__init__(tamano, posicion,r"imagenes\comida.png")
        elif tipo == "puerta":
            super().__init__(tamano, posicion,r"imagenes\puerta.png")

    def actualizar(self,pantalla):
        """
        Brief:Actualiza la representación visual del objeto en la pantalla.
        Parametros: pantalla: La superficie de la pantalla en la que se va a actualizar el objeto.
        """
        self.blit(pantalla)
