import pygame as py
from caracteres.classObjetos import Object
from values.activos import *
from values.colores import *
import random

class CaenObjetos(Object):

    def __init__(self, tamano, tipo="" ,posicion=(0, 0),velocidad = 5) -> None:
        self.tamano = tamano
        self.establecer_velocidad(velocidad)
        self.tipo = tipo
        if tipo == "fuego":
            super().__init__(tamano, posicion,r"imagenes\fuego.png")
        else:
            super().__init__(tamano, posicion,r"imagenes\botiquin.png")

        self.poner_random_posicion()
        velocidad = random.randrange(3,7)
        self.establecer_velocidad(velocidad)
    
    def poner_random_posicion(self):
        """
        Brief: Reposiciona el objeto en una posición aleatoria fuera de la pantalla.
        """
        self.rectangulo.x = random.randrange(self.rectangulo.width, 1200 - self.rectangulo.width)
        self.rectangulo.y = random.randrange(-100,-40)

    def mover_abajo(self):
        """
        Brief:Mueve el objeto hacia abajo, y lo reposiciona si alcanza la parte inferior de la pantalla.
        """
        if self.rectangulo.y > 650:
            self.poner_random_posicion()
        else:
            super().mover_abajo()