import pygame
from pygame.locals import *

from Modulos.Gui.GUI_button_image import *
from Modulos.Gui.GUI_form import *
from Modulos.Gui.GUI_label import *
from Modulos.Values.colores import *

        
class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, scoreboard, margen_y,margen_x, espacio):
        super().__init__(screen, x,y,w,h,color_background,color_border,active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self._score = scoreboard
        self.lista_widgets = []
        self._margen_y = margen_y

        self.lista_widgets.append(
            Label(screen=self._slave, x=margen_x+10,y=20,w=w/2-margen_x-10,h=50,text = "Jugadores", font="Arial Black",font_size=30,font_color=NEGRO,path_image="Modulos\Assets\Imagenes\Menu\Table.png"))
        self.lista_widgets.append(
            Label(screen=self._slave,
                 x=margen_x+10+w/2-margen_x-10,
                 y=20,w=w/2-margen_x-10,
                 h=50,text = "Puntaje",
                font="Arial Black",
                font_size=30,
                font_color= NEGRO,
                path_image="Modulos\Assets\Imagenes\Menu\Table.png"))
        
        pos_inicial_y = margen_y
        
        for j in self._score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = "" 
                cadena = f"{s}"
                pos = Label(screen=self._slave, x=pos_inicial_x,y=pos_inicial_y,
                            w=w/2-margen_x,h=100,text = cadena, font="Arial Black",font_size=30,
                            font_color=NEGRO, path_image="Modulos\Assets\Imagenes\Menu\Table.png")
                self.lista_widgets.append(pos)
                pos_inicial_x += w/2-margen_x
                
            pos_inicial_y+=100 + espacio
                
        # Buttom home
        self._btn_home = Button_Image(screen = self._slave, 
        master_x = x, 
        master_y = y, 
        x = w-50, 
        y = h-50, 
        w = 30, 
        h = 30, 
        path_image = "Modulos\Assets\Imagenes\Menu\home.png", 
        onclick = self.btn_home_click, 
        onclick_param = "")

        self.lista_widgets.append(self._btn_home)
        
    def btn_home_click(self,parametro):
        self.end_dialog()
    
    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        
        