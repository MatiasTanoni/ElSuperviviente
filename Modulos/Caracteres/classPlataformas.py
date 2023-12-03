
from Modulos.Caracteres.classObjetos import *

class Plataforma(Object):
    def __init__(self,tamano,posicion,tipo="visible") -> None:
        if tipo == "visible":
            super().__init__(tamano, posicion,"Modulos\Assets\Imagenes\PLATAFORMA.png")
        else:
            super().__init__(tamano, posicion)

