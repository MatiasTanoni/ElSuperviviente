from Modulos.Gui.GUI_button import *
from Modulos.Gui.GUI_form_container_level import *
from Modulos.Gui.GUI_slider import *
from Modulos.Gui.GUI_textbox import *
from Modulos.Gui.GUI_label import *
from Modulos.Gui.GUI_form import *
from Modulos.Gui.GUI_button_image import *
from Modulos.Gui.GUI_form_menu_score import *
from Modulos.Niveles.ManejadorDeNiveles import *
from pygame.locals import *
import pygame

class FormMenuPause(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, level, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))
        self._slave = aux_image
        self.flag_play = True
        self.level = level
        
        self._label_pause = Label(screen=self._slave,
                          x=100,
                          y=40,
                          w= 200,
                          h= 50,
                          text= "Menu de Pausa",   
                          font= "Arial Black",
                          font_color= NEGRO,
                          font_size= 25,
                          path_image= "Modulos\Assets\Imagenes\Menu\Table.png"  
                        )

        self._btn_unpause = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 300,
                        y = self._h - 150,
                        w = 200,
                        h = 80,
                        onclick = self.btn_unpause_click,
                        onclick_param = "",
                        path_image = "Modulos\Assets\Imagenes\Menu\Table.png",
                        text = "Continue",
                        font = "Arial Black",
                        font_size = 25) 
        
        self.lista_widgets.append(self._label_pause)
        self.lista_widgets.append(self._btn_unpause)
    
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, events):
        if self.level.pause:
            if self.verificar_dialog_result():
                for widget in self.lista_widgets:
                    widget.update(events)
                self.draw() 
            else:
                self.hijo.update(events)
            
    def btn_unpause_click(self, param):
        self.level.resume_game()
        self.level.play_music()
        self.end_dialog()
    
    def btn_home_click(self, param):
        del self.level
        self.end_dialog()