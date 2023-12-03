import re
import pygame
from pygame.locals import *

from Modulos.Gui.GUI_button import *
from Modulos.Gui.GUI_form_container_level import *
from Modulos.Gui.GUI_slider import *
from Modulos.Gui.GUI_textbox import *
from Modulos.Gui.GUI_label import *
from Modulos.Gui.GUI_form import *
from Modulos.Gui.GUI_button_image import *
from Modulos.Gui.GUI_form_menu_score import *
from Modulos.Niveles.ManejadorDeNiveles import *
from Modulos.Assets.Musica import *


    
class FormMenuPlay(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        self.manejador_niveles = ManejadorDeNiveles()  
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))
        self._slave = aux_image

        # TextBox Name
        self._box_name = TextBox(screen=self._slave,
                          master_x=x,
                          master_y=y,
                          x=90,
                          y=50,
                          w= 230,
                          h= 50,
                          color_background = BLANCO,
                          color_background_seleccionado= AMARILLO,
                          color_border= AMARILLO,
                          color_border_seleccionado= BLANCO,
                          border_size= 4, 
                          font= "Arial Black",
                          font_color= NEGRO,
                          font_size= 20,

                        )

        # Button Level One
        self._btn_level_1 = Button_Image(screen=self._slave,
                            master_x=x,
                            master_y=y,
                            x=100,
                            y=110,
                            w= 200,
                            h= 80,
                            onclick= self.create_level,
                            onclick_param= "level_one",
                            path_image= "Modulos\Assets\Imagenes\Menu\Table.png",
                            text = "Nivel Uno",
                            font = "Arial Black",
                            font_size = 25,
                            font_color = NEGRO)
        
        # Button Level Two
        self._btn_level_2 = Button_Image(screen=self._slave,
                            master_x= x,
                            master_y=y,
                            x=100,
                            y=200,
                            w=200,
                            h=80,
                            onclick= self.create_level,
                            onclick_param= "level_two",
                            path_image= "Modulos\Assets\Imagenes\Menu\Table.png",
                            text = "Nivel Dos",
                            font = "Arial Black",
                            font_size = 25,
                            font_color = NEGRO)
        
        # Button Level Three
        self._btn_level_3 = Button_Image(screen=self._slave,
                            master_x= x,
                            master_y=y,
                            x=100,
                            y=290,
                            w= 200,
                            h= 80,
                            onclick= self.create_level,
                            onclick_param= "level_three",
                            path_image= "Modulos\Assets\Imagenes\Menu\Table.png",
                            text = "Nivel Tres",
                            font = "Arial Black",
                            font_size = 25,
                            font_color = NEGRO)
        
        # Button Home
        self._btn_home = Button_Image(screen=self._slave,
                            master_x = self._x,
                            master_y= self._y,
                            x = self._w - 50,
                            y = self._h - 50,
                            w= 30,
                            h= 30,
                            onclick= self.btn_home_click,
                            onclick_param= "",
                            path_image= "Modulos\Assets\Imagenes\Menu\home.png")
        
        self.lista_widgets.append(self._box_name)
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
    
    def render(self):
        self._slave.fill(self._color_background)

    def sanitize_name(self):
        """
        Brief: Sanitiza un nombre ingresado en un contexto de interfaz gráfica.

        Descripción:
            Este método toma el texto ingresado en un cuadro de entrada de la GUI, elimina dígitos numéricos,
            convierte el texto a formato de título y elimina espacios en blanco al principio y al final.

        Parámetros:
            Ninguno

        Retorno:
            str: El nombre sanitizado si no está vacío, de lo contrario, devuelve "N/A".
        """
        name_entered = self._box_name.get_text()
        cadena = re.sub("[0-9]+", "", name_entered)
        cadena = cadena.title()
        name = cadena.strip()

        if len(name) != 0:
            return name
        else:
            return "Incognito"
 
    def update(self, events):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(events)
            self.draw()  
        else:
            self.hijo.update(events)

    def create_level(self, level_name):
        pygame.mixer.music.pause()
        name = self.sanitize_name()
        nivel = self.manejador_niveles.get_level(level_name)
        frm_contenedor_nivel = FormContainerLevel(self._master, nivel, name)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()