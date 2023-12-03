import pygame as py
from Modulos.Caracteres.classObjetos import Object
from Modulos.Values.activos import *
from Modulos.Values.colores import *


class Item(Object):

    def __init__(self, tamano, tipo="", posicion=(0, 0)) -> None:
        self.tamano = tamano
        self.tipo = tipo
        if tipo == "agua":
            super().__init__(tamano, posicion,r"Modulos\Assets\Imagenes\agua.png")
        elif tipo == "comida":
            super().__init__(tamano, posicion,r"Modulos\Assets\Imagenes\comida.png")
        elif tipo == "puerta":
            super().__init__(tamano, posicion,r"Modulos\Assets\Imagenes\puerta.png")

    def actualizar(self,pantalla):
        """
        Brief:Actualiza la representación visual del objeto en la pantalla.
        Parametros: pantalla: La superficie de la pantalla en la que se va a actualizar el objeto.
        """
        self.blit(pantalla)
