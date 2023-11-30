import pygame as py
from caracteres.classObjetos import Object

class Disparo(Object):
    def __init__(self,tamano,posicion,direccion) :
        super().__init__(tamano,posicion,r"imagenes\piedra.png")
        self.direccion = direccion

    def actualizar(self):
        """
        Brief:Actualiza la posición del objeto según su dirección.
        """
        if self.direccion == "Izquierda":
            self.rectangulo.x -= 15
        else :
            self.rectangulo.x += 15