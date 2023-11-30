import pygame as py
from caracteres.classObjetos import Object
from values.activos import *
from values.colores import *


class Jefe(Object):

    def __init__(self, tamano, rango_de_movimiento,posicion=(0, 0),velocidad=5) -> None: 
        self.rango_de_movimiento = rango_de_movimiento
        self.tamano = tamano
        self.vidas = 5
        self.contador_de_pasos = 0
        self.animaciones = self.cargar_animaciones()
        self.que_hace = "Derecha"
        self.animacion_actual = self.animaciones[self.que_hace]

        self.establecer_velocidad(velocidad)

        super().__init__(tamano, posicion,self.animacion_actual[self.contador_de_pasos])

    def animar(self,pantalla:py.Surface):
        """
        Brief:Realiza la animación del personaje en la pantalla.
        Parametros:pantalla: La superficie de la pantalla en la que se realiza la animación.
        """
        pantalla.blit(self.animacion_actual[self.contador_de_pasos],self.rectangulo)

    def verificar_accion(self, pantalla: py.Surface):
        """
        Brief:Verifica y realiza la acción correspondiente del personaje, actualizando su posición y animación.
        Parametros:pantalla: La superficie de la pantalla en la que se realiza la acción.
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
        Retorno:animaciones: Un diccionario que contiene listas de imágenes para las animaciones de derecha e izquierda.
        """
        lista_personaje_derecha = []
        lista_personaje_izquierda= []
        lista_rutas = [r"imagenes\jefe_der.png",]
        lista_rutas_izquierda = [r"imagenes\jefe_izq.png"]

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
        Brief:Actualiza la pantalla, donde si tiene mas de 0 vidas el jefe puede utilizar
        la funcion verificar_accion().
        Parametros:pantalla: La superficie de la pantalla en la que se va a actualizar.
        """
        if self.vidas > 0 :
            self.verificar_accion(pantalla)


