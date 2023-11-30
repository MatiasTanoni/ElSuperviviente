import sys
import pygame as py
from pygame.locals import *


from caracteres.classPersonaje import Personaje
from datos import inserta_datos_jugador, obtener_top_puntajes
from niveles.classNivelDos import NivelDos
from niveles.classNivelTres import NivelTres
from niveles.nivel_uno import NivelUno
from values.activos import *
from values.colores import *

###############################################
def ventana(tamaño,titulo,icono):
    """
    Brief: 
        Crea una ventana
    Parametros:
        tamaño = el tamaño de la ventana
        titulo = el titulo de la ventana
        icono = el icono de la ventana
    Retorno:
        ventana
    """
    ventana = py.display.set_mode(tamaño)
    py.display.set_caption(titulo)
    py.display.set_icon(icono)

    return ventana


def crear_menu():
    """
    Brief: 
        Crea un menú.
    Retorno:
        True, si se clickea dentro del rango del boton start
    """
    imagen_icono = py.image.load("imagenes/icono.png")
    imagen_menu = py.image.load("imagenes\menu.png")
    imagen_menu = py.transform.scale(imagen_menu,(1200,650))
    imagen_zombie = py.image.load("imagenes\Palabra_Zombie.png")
    imagen_zombie = py.transform.scale(imagen_zombie,(300,240))

    imagen_nivel_1 = py.image.load("imagenes\level 1.png")
    imagen_nivel_1 = py.transform.scale(imagen_nivel_1,(80,60))
    
    imagen_nivel_2 = py.image.load("imagenes\level 2.png")
    imagen_nivel_2 = py.transform.scale(imagen_nivel_2,(70,60))

    imagen_nivel_3 = py.image.load("imagenes\level 3.png")
    imagen_nivel_3 = py.transform.scale(imagen_nivel_3,(70,60))

    MENU = ventana((1200,650),"Menú",imagen_icono)  
                        
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                x, y = py.mouse.get_pos()
                if start_rectangulo_1.collidepoint(x,y):
                    return 0
                elif start_rectangulo_2.collidepoint(x,y):
                    return 1
                elif start_rectangulo_3.collidepoint(x,y):
                    return 2
        MENU.blit(imagen_menu, [0, 0])
        MENU.blit(imagen_zombie,[900,30])
        start_rectangulo_1 = MENU.blit(imagen_nivel_1,[900,320]) 
        start_rectangulo_2 = MENU.blit(imagen_nivel_2,[1000,320]) 
        start_rectangulo_3 = MENU.blit(imagen_nivel_3,[1100,320]) 

        py.display.update()

###############################################
py.init()
nivel_tres = NivelTres((1200,650))
nivel_dos = NivelDos((1200,650))
nivel_uno = NivelUno((1200,650))
niveles = [nivel_uno,nivel_dos,nivel_tres]
dict = {}
dict["clave"] = crear_menu()

def finalizar_nivel():
    """
    Brief: Verifica si el personaje ha alcanzado la puerta y completa el nivel.
    """
    for item in niveles[dict["clave"]].items:
        if item.rectangulo.colliderect(niveles[dict["clave"]].personaje.rectangulo):
            if item.tipo == "puerta":
                inserta_datos_jugador("mi_base_de_datos.db","matias",niveles[dict["clave"]].personaje.puntos)
                niveles[dict["clave"]].estado = "completado"

flag = True
while flag:

    niveles[dict["clave"]].clock.tick(nivel_tres.FPS)
    eventos = py.event.get()    
    for event in eventos:
        if event.type == QUIT:
            flag = False  
    finalizar_nivel() 
    if niveles[dict["clave"]].estado != "completado": 
        niveles[dict["clave"]].actualizar(eventos)
        if niveles[dict["clave"]].personaje.vidas <= 0 or niveles[dict["clave"]].tiempo_restante <= 0:
            del niveles[dict["clave"]]
            nivel_tres = NivelTres((1200,650))
            nivel_dos = NivelDos((1200,650))
            nivel_uno = NivelUno((1200,650))
            niveles = [nivel_uno,nivel_dos,nivel_tres]
            dict["clave"] = crear_menu()
    elif niveles[dict["clave"]].personaje.vidas <= 0 or niveles[dict["clave"]].tiempo_restante <= 0 or niveles[dict["clave"]].estado == "completado":
        del niveles[dict["clave"]]      
        nivel_tres = NivelTres((1200,650))
        nivel_dos = NivelDos((1200,650))
        nivel_uno = NivelUno((1200,650))
        niveles = [nivel_uno,nivel_dos,nivel_tres]
        dict["clave"] = crear_menu()
    else:  
        break
    diccionario = []
    result = obtener_top_puntajes("mi_base_de_datos.db")
    for fila in result:
        diccionario.append({fila[0], fila[1]})
        niveles[dict["clave"]].aplicar_mensaje(f"TOP PUNTAJE: Nombre: {fila[0]}, Puntos: {fila[1]}",10,610,BLANCO,20,"Arial Black")
    py.display.update()

py.quit()       
###############################################
