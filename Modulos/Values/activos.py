import os
import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    """
    Brief: Escala todas las imágenes en un diccionario de animaciones al tamaño especificado.
    
    Parámetros:
        - diccionario_animaciones (dict): Diccionario con animaciones a escalar.
        - ancho (int): Ancho deseado para las imágenes escaladas.
        - alto (int): Alto deseado para las imágenes escaladas.

    Modifica:
        - diccionario_animaciones (dict): Imágenes escaladas sustituyen a las originales.
    """
    for clave in diccionario_animaciones:
        lista = diccionario_animaciones[clave]
        for i in range(len(lista)):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    """
    Brief: Genera una lista de imágenes rotadas horizontalmente.
    
    Parámetros:
        - imagenes (list): Lista de imágenes a rotar.

    Retorno:
        - lista_imagenes (list): Lista que contiene las imágenes rotadas horizontalmente.
    """
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes


