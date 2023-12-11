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
import pygame as py


    
class FormMenuOptions(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        aux_image = py.image.load(path_image)
        aux_image = py.transform.scale(aux_image, (w,h))
        self._slave = aux_image
        self.flag_play = True
        self.volumen = 0.1

        self._label_tittle = Label(screen=self._slave,
                          x= 80,
                          y= 40,
                          w= 250,
                          h= 50,
                          text= "Configuraciones",   
                          font= "Arial Black",
                          font_color= NEGRO,
                          font_size= 25,
                          path_image= "Modulos\Assets\Imagenes\Menu\Table.png"  
                        )

        self.btn_play_music = Button_Image(self._slave, 
                                        x, 
                                        y, 
                                        350, 
                                        20, 
                                        30, 
                                        30,
                                        "Modulos\Assets\Imagenes\Menu\sound.png",
                                        self.btn_play_click, 
                                        "")

        self.slider_volumen = Slider(self._slave, 
                                            x, 
                                            y, 
                                            80, 
                                            150, 
                                            200, 
                                            15, 
                                            self.volumen, 
                                            BLANCO, 
                                            VERDE)
        
        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave, 
                                            285, 
                                            130, 
                                            50, 
                                            50, 
                                            porcentaje_volumen, 
                                            "Arial Black", 
                                            15, 
                                            NEGRO,
                                            "Modulos\Assets\Imagenes\Menu\Table.png")
        
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
        
        self.lista_widgets.append(self._label_tittle)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_play_music)
        self.lista_widgets.append(self._btn_home)

    
    def render(self):
        self._slave.fill(self._color_background)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.actualizar(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        py.mixer.music.set_volume(self.volumen)

    def btn_play_click(self, param):
        if self.flag_play:
            py.mixer.music.pause()
        else:
            py.mixer.music.unpause()

        self.flag_play = not self.flag_play

    def actualizar(self, events):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.actualizar(events)
            self.update_volumen(events) 
            self.draw() 
            self.render()
        else:
            self.hijo.actualizar(events)

    def btn_home_click(self, param):
        self.end_dialog()
    
