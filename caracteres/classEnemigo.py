import pygame as py
from caracteres.classObjetos import Object
from values.activos import *
from values.colores import *


class Enemigo(Object):

    def __init__(self, tamano, rango_de_movimiento,posicion=(0, 0),velocidad=5) -> None: 
        self.rango_de_movimiento = rango_de_movimiento
        self.tamano = tamano
        self.contador_de_pasos = 0
        self.animaciones = self.cargar_animaciones()
        self.que_hace = "Derecha"
        self.animacion_actual = self.animaciones[self.que_hace]

        self.establecer_velocidad(velocidad)

        super().__init__(tamano, posicion,self.animacion_actual[self.contador_de_pasos])

    def animar(self,pantalla:py.Surface):
        """
        Brief:Realiza la animación en la pantalla.
        Parametros:pantalla: Superficie de pantalla en la que se realiza la animación (tipo: pygame.Surface).
        """
        pantalla.blit(self.animacion_actual[self.contador_de_pasos],self.rectangulo)

    def verificar_accion(self, pantalla: py.Surface):
        """
        Brief:Verifica y realiza la acción del enemigo en la pantalla.
        Parámetros:pantalla: La pantalla del juego.
        """  
        match self.que_hace:
            case "Derecha":
                self.animacion_actual = self.animaciones["Derecha"]
                self.rectangulo.x += self.velocidad 
                self.animar(pantalla)
                if self.rectangulo.x > self.rango_de_movimiento[1]:
                    self.que_hace = "Izquierda"
            case "Izquierda":
                self.animacion_actual = self.animaciones["Izquierda"]
                self.rectangulo.x -= self.velocidad 
                self.animar(pantalla)
                if self.rectangulo.x < self.rango_de_movimiento[0]:
                    self.que_hace = "Derecha"

    def cargar_animaciones(self):
        """
        Brief:Carga las animaciones del personaje.
        Retorno:animaciones: Diccionario con las animaciones del personaje.
        """

        lista_personaje_derecha = []
        lista_personaje_izquierda= []
        lista_rutas = [r"imagenes\zombie.png",]
        lista_rutas_izquierda = [r"imagenes\zombie_izq.png"]

        for path in lista_rutas:
            imagen_enemigo_derecha = self.cargar_imagen(path, self.tamano) 
            lista_personaje_derecha.append(imagen_enemigo_derecha)
        
        for path in lista_rutas_izquierda:
            imagen_enemigo_izquierda = self.cargar_imagen(path, self.tamano) 
            lista_personaje_izquierda.append(imagen_enemigo_izquierda)

        animaciones = {}
        animaciones["Derecha"] = lista_personaje_derecha
        animaciones["Izquierda"] = lista_personaje_izquierda

        return animaciones

    def actualizar(self,pantalla):
        """
        Brief:Actualiza el objeto verificando su acción en la pantalla.
        Parámetros:pantalla: La pantalla del juego.
        """
        self.verificar_accion(pantalla)


