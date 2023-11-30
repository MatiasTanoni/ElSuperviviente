import pygame as py
from caracteres.classDisparo import Disparo
from caracteres.classObjetos import Object
from values.activos import *
from values.colores import *

class Personaje(Object):

    def __init__(self, tamano, posicion=(0, 0),velocidad=5) -> None:
        
        self.posicion = posicion
        self.vidas = 3
        self.tamano = tamano
        self.contador_de_pasos = 0
        self.puntos = 0
        self.animaciones = self.cargar_animaciones()
        self.que_hace = "Quieto"
        self.animacion_actual = self.animaciones[self.que_hace]

        self.establecer_velocidad(velocidad)

        self.desplazamiento_y = 0
        self.potencia_salto = -16
        self.limite_velocidad_salto = 16
        self.gravedad = 1
        self.esta_saltando = False

        self.flag_disparo = False
        self.tiempo_ultimo_disparo = 0
        self.lista_proyectiles = []

        super().__init__(tamano, posicion,self.animacion_actual[self.contador_de_pasos])
        
    def animar(self,pantalla:py.Surface):
        """
        Brief:Realiza la animación del personaje en la pantalla.
        Parametros:pantalla: La superficie de la pantalla en la que se realiza la animación.
        """
        if self.contador_de_pasos >= len(self.animacion_actual):
            self.contador_de_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_de_pasos],self.rectangulo)
        self.contador_de_pasos += 1

    def verificar_evento(self):
        """
        Brief:Verifica las teclas presionadas y actualiza la acción del personaje.
        """
        teclas = py.key.get_pressed()
        if teclas[py.K_RIGHT]:
            self.que_hace = "Derecha"
        elif teclas [py.K_LEFT]:
            self.que_hace = "Izquierda"
        elif teclas [py.K_UP]:
            self.que_hace = "Salta"
        else:
            self.que_hace = "Quieto"

        if self.flag_disparo and teclas[py.K_f]:
            tiempo_actual = py.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo >= 1000:
                self.lanzar_proyectil()
                self.efectos_de_sonido(r"sonidos\sonido de disparo.mp3",0.2)
                self.flag_disparo = False
                self.tiempo_ultimo_disparo = tiempo_actual

    def lanzar_proyectil(self):
        """
        Brief: Lanza un proyectil desde la posición del personaje en la dirección actual.
        """
        x = None
        margen = 47

        y = self.rectangulo.centery + 10
        if self.que_hace == "Derecha":
            x = self.rectangulo.right - margen
        elif self.que_hace == "Izquierda":
            x = self.rectangulo.left - 100 + margen
            
        if x is not None:
            print(self.que_hace)
            self.lista_proyectiles.append(Disparo((20,20),(x,y),self.que_hace))

    def actualizar_proyectiles(self, pantalla):
        """
        Brief:Actualiza y muestra en pantalla los proyectiles del personaje.
        Parametros: pantalla: La superficie de la pantalla en la que se actualizan los proyectiles.
        """
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            pantalla.blit(p.image, p.rectangulo)
            p.actualizar()
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1
            
    def verificar_accion(self, pantalla: py.Surface,plataformas):
        """
        Brief:Verifica y realiza la acción correspondiente del personaje, actualizando su posición y animación.
        Parametros:pantalla: La superficie de la pantalla en la que se realiza la acción.
                plataformas: Lista de plataformas en el juego.
        """
        self.verificar_evento()
        match self.que_hace:
            case "Derecha":                                                 #PARA CAMBIAR DE DIRECCION
                    self.animacion_actual = self.animaciones["Derecha"]
                    self.animar(pantalla)
                    self.mover_derecha(1204)
                    self.flag_disparo = True
            case "Izquierda":
                    self.animacion_actual = self.animaciones["Izquierda"]
                    self.animar(pantalla)
                    self.mover_izquierda(0)
                    self.flag_disparo = True
            case "Quieto":
                self.animacion_actual = self.animaciones["Quieto"]
                self.animar(pantalla)
            case "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["Salta"]
                    self.mover_arriba(0)

        self.aplicar_gravedad(pantalla,plataformas)

    def cargar_animaciones(self):
        """
        Brief:Carga las animaciones del personaje.
        Retorno:animaciones:Un diccionario que contiene listas de imágenes para las animaciones de quieto, derecha, izquierda y salta.
        """
        lista_personaje_quieto = []
        lista_personaje_derecha = []
        lista_personaje_salta = []
        lista_rutas = [r"imagenes\DERECHa.png",r"imagenes\DERECha_2.png",r"imagenes\DERECHA 3.png",r"imagenes\DERECHA 4.png",r"imagenes\DERECHA 5.png",r"imagenes\DERECHA 6.png"]
        lista_rutas_2 = [r"imagenes\saltandoo.png",r"imagenes\saltando_2.png"]
        lista_rutas_3 = [r"imagenes\quieto1.png",r"imagenes\quieto1.png",r"imagenes\quieto2.png",r"imagenes\quieto2.png",r"imagenes\quieto3.png",r"imagenes\quieto3.png",r"imagenes\quieto4.png",r"imagenes\quieto4.png",r"imagenes\quieto5.png",r"imagenes\quieto5.png",r"imagenes\quieto6.png",r"imagenes\quieto6.png",r"imagenes\quieto7.png",r"imagenes\quieto7.png"]

        for path in lista_rutas:
            image_hero_walk_right = self.cargar_imagen(path, self.tamano) 
            lista_personaje_derecha.append(image_hero_walk_right)

        for path in lista_rutas_2:
            imagen_saltando = self.cargar_imagen(path, (self.tamano[0] + 30, self.tamano[1] + 10))
            lista_personaje_salta.append(imagen_saltando)

        for path in lista_rutas_3:
            imagen_quieto = self.cargar_imagen(path, self.tamano)
            lista_personaje_quieto.append(imagen_quieto)

        animaciones = {}
        animaciones["Quieto"] = lista_personaje_quieto
        animaciones["Derecha"] = lista_personaje_derecha
        animaciones["Izquierda"]  = rotar_imagen(lista_personaje_derecha)
        animaciones["Salta"] = lista_personaje_salta

        return animaciones

    def aplicar_gravedad(self, pantalla, plataformas):
        """
        Brief:Aplica la gravedad al objeto mientras salta y detecta colisiones con plataformas.
        Parametros: pantalla: La superficie de la pantalla en la que se aplica la gravedad.
                    plataformas: Lista de plataformas en el juego.
        """
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
    
        for pl in plataformas:
                if self.rectangulo.colliderect(pl.rectangulo):
                    if self.desplazamiento_y > 0:
                        self.desplazamiento_y = 0
                        self.esta_saltando = False
                        self.rectangulo.bottom = pl.rectangulo.top
                    elif self.desplazamiento_y < 0: 
                        self.desplazamiento_y = 0
                        self.rectangulo.top = pl.rectangulo.bottom
                    break
                else:
                    self.esta_saltando = True


    def actualizar(self,pantalla,plataformas,enemigos,bombitas,objetos_que_caen,comidas,jefe=None):
        """
        Brief:Actualiza la pantalla, donde si tiene mas de 0 vidas el jefe puede utilizar
        la funcion verificar_accion().
        Parametros:pantalla: La superficie de la pantalla en la que se va a actualizar.
        """
        self.verificar_accion(pantalla,plataformas)
        self.colisionar(enemigos,bombitas,objetos_que_caen,comidas,jefe)
        self.mostrar_vida(pantalla)  
        self.actualizar_proyectiles(pantalla)

    def mover_derecha(self, ancho): 
        """
        Brief:un límite a la derecha de la pantalla.
        Parametros: tope: El valor mínimo para la coordenada x.
        """
        nueva_x = self.rectangulo.x+ self.velocidad
        
        if nueva_x >= 0 and nueva_x <= ancho - self.rectangulo.width:
            self.image = self.animacion_actual
            super().mover_derecha()

    def mover_izquierda(self, ancho_izquierda):
        """
        Brief:un límite a la izquierda de la pantalla.
        Parametros: tope: El valor mínimo para la coordenada x.
        """
        nueva_x = self.rectangulo.x - self.velocidad

        if nueva_x >= ancho_izquierda:
            self.image= self.animacion_actual

            super().mover_izquierda()

    def mover_arriba(self, tope):
        """
        Brief:un límite superior.
        Parametros: tope: El valor mínimo para la coordenada y.
        """
        nueva_y = self.rectangulo.y - self.velocidad

        if nueva_y >= tope:
            self.image = self.animacion_actual

            super().mover_arriba()

    def colisionar(self,enemigos,bombitas,objetos_que_caen,items,jefe):
        """
        Brief:Maneja las colisiones del personaje con diversos elementos del juego, actualizando vidas y puntajes.
        Parametros: enemigos: Lista de enemigos en el juego.
                bombitas: Lista de bombas en el juego.
                objetos_que_caen: Lista de objetos que caen en el juego.
                items: Lista de items en el juego.
                jefe: Jefe en el juego.
        """
        for enemigo in enemigos:
            if self.rectangulo.colliderect(enemigo.rectangulo):
                self.vidas -= 1
                self.rectangulo.x = 900
                self.rectangulo.y = 460
                self.efectos_de_sonido(r"sonidos\Die-Sound-Effect.mp3",0.2)
        for bomba in bombitas:
            if self.rectangulo.colliderect(bomba.rectangulo):
                bombitas.remove(bomba)
                self.vidas -= 1
                self.rectangulo.x = 900
                self.rectangulo.y = 460
                self.efectos_de_sonido(r"sonidos\Die-Sound-Effect.mp3",0.2)
        for obj in objetos_que_caen:
            if self.rectangulo.colliderect(obj.rectangulo):
                if obj.tipo == "fuego":
                    objetos_que_caen.remove(obj)
                    self.vidas -= 1
                    self.rectangulo.x = 900
                    self.rectangulo.y = 460
                    self.efectos_de_sonido(r"sonidos\Die-Sound-Effect.mp3",0.2)
                else:
                    self.efectos_de_sonido(r"sonidos\sonido de items.mp3",0.2)
                    if self.vidas < 3:
                        self.vidas += 1  
                    objetos_que_caen.remove(obj) 
        for item in items:
            if self.rectangulo.colliderect(item.rectangulo):             
                if item.tipo == "agua":
                    self.puntos += 1
                    items.remove(item)
                    self.efectos_de_sonido(r"sonidos\sonido de items.mp3",0.2)
                elif item.tipo == "comida":
                    self.puntos += 2
                    items.remove(item)
                    self.efectos_de_sonido(r"sonidos\sonido de items.mp3",0.2)
                else:
                    self.efectos_de_sonido(r"sonidos\WIN-sound-effect-no-copyright.mp3",0.2)
        for proyectil in self.lista_proyectiles:
            for enemigo in enemigos:
                if proyectil.rectangulo.colliderect(enemigo.rectangulo):
                    self.efectos_de_sonido(r"sonidos\cuando_muere_un_enemigo.mp3",0.1)
                    enemigos.remove(enemigo)
                    self.puntos += 1
                    self.lista_proyectiles.remove(proyectil)
        try:                 
            if proyectil.rectangulo.colliderect(jefe.rectangulo):
                jefe.vidas -= 1
                self.lista_proyectiles.remove(proyectil)
                if jefe.vidas <= 0:
                    self.efectos_de_sonido(r"sonidos\cuando_muere_un_enemigo.mp3",0.1)
                    self.puntos += 5
            if jefe.rectangulo.colliderect(self.rectangulo):
                self.efectos_de_sonido(r"sonidos\Die-Sound-Effect.mp3",0.2)
                self.vidas -= 1
                self.rectangulo.x = 900
                self.rectangulo.y = 460
        except AttributeError:
            pass
        except UnboundLocalError:
            pass
    

    def mostrar_vida(self,pantalla):
        """
        Brief:Muestra la representación visual de las vidas del objeto en la pantalla.
        Parametros: pantalla: La superficie de la pantalla en la que se muestra la vida.
        """
        vida1 = self.cargar_imagen(r"imagenes\full vida.png",(160,40))
        vida2 = self.cargar_imagen(r"imagenes\vida 3,4.png",(160,40))
        vida3 = self.cargar_imagen(r"imagenes\vida 2,4.png",(160,40))
        vida4 = self.cargar_imagen(r"imagenes\0_de_vida.png",(160,40))
        if self.vidas == 3:
            pantalla.blit(vida1,(1000,5))
        elif self.vidas == 2:
            pantalla.blit(vida2,(1000,5))
        elif self.vidas == 1:
            pantalla.blit(vida3,(1000,5))
        else:
            pantalla.blit(vida4,(1000,5))