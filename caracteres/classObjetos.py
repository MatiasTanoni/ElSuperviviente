import pygame as py
from values.activos import *
from values.eorientation import EOrientation


class Object:

    def __init__(self, tamano_superficie, posicion, animacion=None) -> None:
        if type(animacion) == py.surface.Surface:
            self.image = animacion
        elif animacion == None:
            self.image = py.Surface(tamano_superficie,-1)
        else:
            self.image = self.cargar_imagen(animacion, tamano_superficie)

        self.rectangulo = self.image.get_rect()

        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]

        self.direccion = EOrientation.IDLE

    def cargar_imagen(self, ruta, tamano_superficie):
        """
        Brief:Carga una imagen en especifico
        Parametros:ruta: La ruta de la imagen
                tamano_superficie: el tamaño de la imagen
        """
        imagen = py.image.load(ruta)
        imagen = py.transform.scale(imagen, tamano_superficie)

        return imagen

    def establecer_velocidad(self, velocidad):
        """
        Brief:Establece la velocidad.
        Parametros:velocidad: La velocidad para este movimiento.
        """
        self.velocidad = velocidad

    def mover_arriba(self, velocidad=None):
        """
        Brief:Mueve el objeto hacia arriba con la velocidad especificada.
        Parametros:velocidad: La velocidad opcional para este movimiento.
        """
        if velocidad:
            self.establecer_velocidad(velocidad=None)

        self.direccion = EOrientation.UP
        self.mover()

    def mover_abajo(self, velocidad=None):
        """
        Brief:Mueve el objeto hacia abajo con la velocidad especificada.
        Parametros:velocidad: La velocidad opcional para este movimiento.
        """
        if velocidad:
            self.establecer_velocidad(velocidad)

        self.direccion = EOrientation.DOWN
        self.mover()

    def detener(self):
        """
        Brief:Detiene el movimiento del objeto.
        """
        self.direccion = EOrientation.IDLE
        self.mover()

    def mover_derecha(self, velocidad=None):
        """
        Brief:Mueve el objeto hacia la derecha con la velocidad especificada.
        Parametros:velocidad: La velocidad opcional para este movimiento.
        """
        if velocidad:
            self.establecer_velocidad(velocidad=None)
        self.direccion = EOrientation.RIGHT
        self.mover()

    def mover_izquierda(self, velocidad=None):
        """
        Brief:Mueve el objeto hacia la izquierda con la velocidad especificada.
        Parametros:velocidad: La velocidad opcional para este movimiento.
        """
        if velocidad:
            self.establecer_velocidad(velocidad=None)
        self.direccion = EOrientation.LEFT
        self.mover()

    def mover(self):
        """
        Brief:Mueve el objeto en la dirección especificada.
        ValueError: Si la dirección es inválida.
        """
        if self.direccion == EOrientation.LEFT:
            self.rectangulo.x -= self.velocidad              
        elif self.direccion == EOrientation.RIGHT:
            self.rectangulo.x += self.velocidad
        elif self.direccion == EOrientation.UP:
            self.rectangulo.y -= self.velocidad
        elif self.direccion == EOrientation.DOWN:
            self.rectangulo.y += self.velocidad
        elif self.direccion == EOrientation.IDLE:
            pass
        else:
            raise ValueError('Dirección inválida')

    def blit(self, pantalla):
        """
        Brief:Copia la imagen del objeto en la superficie de la pantalla.
        Parametros:pantalla: La superficie de la pantalla en la que se realiza la copia.
        """
        pantalla.blit(self.image, self.rectangulo)

    def efectos_de_sonido(self, ruta, volumem):
        """
        Brief: Reproduce un efecto de sonido.
            Este método carga y reproduce un efecto de sonido desde el archivo especificado en "path".
            Se puede ajustar el volumen mediante el parámetro "volume".
        Parámetros:
            path (str): La ruta al archivo de sonido.
            volume (float): El volumen del sonido, un valor entre 0.0 (sin sonido) y 1.0 (volumen máximo).
        """
        musica = py.mixer.Sound(ruta)
        musica.set_volume(volumem)
        musica.play()
    
