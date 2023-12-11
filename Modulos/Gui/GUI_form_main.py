from Modulos.Assets.Musica import *
from Modulos.Data.Data import obtener_top_puntaje
from Modulos.Gui.GUI_form_container_level import *
from Modulos.Gui.GUI_form_menu_options import *
from Modulos.Gui.GUI_form_menu_score import *
from Modulos.Gui.GUI_form_menu_play import *
from Modulos.Gui.GUI_button_image import *
from Modulos.Gui.GUI_textbox import *
from Modulos.Gui.GUI_button import *
from Modulos.Gui.GUI_slider import *
from Modulos.Values.colores import *
from Modulos.Gui.GUI_label import *
from Modulos.Gui.GUI_form import *
from pygame.locals import *
import pygame as py


    
class FormMain(Form):
    def __init__(self,screen,x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)
        self.exit = False
        self.volume = 0.1
        pygame.mixer.init()
        pygame.mixer.music.load(r"Modulos\Assets\Musica\background.mp3")
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
        
        self._label_main = Label(screen=self._slave,
                          x=80,
                          y=40,
                          w= 250,
                          h= 50,
                          text= "Menu Principal",   
                          font= "Arial Black",
                          font_color= NEGRO,
                          font_size= 25,
                          path_image= "Modulos\Assets\Imagenes\Menu\Table.png"  
                        )

        # Button puntaje
        self.btn_scores = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            205, 
                                            200, 
                                            80, 
                                            "Modulos\Assets\Imagenes\Menu\Table.png", 
                                            self.btn_scores_click, 
                                            "",
                                            "Puntajes",
                                            "Arial Black",
                                            25)
        
        # Button Niveles
        self.btn_levels = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            110, 
                                            200, 
                                            80, 
                                            "Modulos\Assets\Imagenes\Menu\Table.png", 
                                            self.btn_levels_click, 
                                            "",
                                            "Niveles",
                                            "Arial Black",
                                            25)
        


        # Button salir
        self.btn_quit = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            300, 
                                            200, 
                                            80, 
                                            "Modulos\Assets\Imagenes\Menu\Table.png", 
                                            self.btn_quit_click, 
                                            "hola",
                                            "Salir",
                                            "Arial Black",
                                            25)
        
        # Button Config
        self.btn_config = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            335, 
                                            20, 
                                            40, 
                                            40, 
                                            "Modulos\Assets\Imagenes\Menu\config.png", 
                                            self.btn_config_click, 
                                            "hola")

        self.lista_widgets.append(self._label_main)
        self.lista_widgets.append(self.btn_scores)
        self.lista_widgets.append(self.btn_levels)
        self.lista_widgets.append(self.btn_quit)
        self.lista_widgets.append(self.btn_config)
    
    def render(self):
        self._slave.fill(self._color_background)

    def actualizar(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.actualizar(lista_eventos)
        else:
            self.hijo.actualizar(lista_eventos)

    def btn_scores_click(self, param):
        diccionario = []
        
        result = obtener_top_puntaje("Modulos\Data\puntaje.db")
        for row in result:
            diccionario.append({"Jugador": row[0], "Puntaje": row[1]})
        
        nuevo_form = FormMenuScore(screen = self._master, 
        x = 400, 
        y = 40, 
        w = 425, 
        h = 450, 
        color_background = BLANCO, 
        color_border = VERDE, 
        active = True, 
        path_image = "Modulos\Assets\Imagenes\Menu\Window.png", 
        scoreboard = diccionario, 
        margen_x = 10, 
        margen_y = 100, 
        espacio = 10
        )

        self.show_dialog(nuevo_form)
    
    def btn_levels_click(self, param):
        menu_play = FormMenuPlay(self._master, 
        x= 400, 
        y= 25, 
        w= 400, 
        h= 400, 
        color_background = BLANCO, 
        color_border =  BLANCO, 
        active = True, 
        path_image = "Modulos\Assets\Imagenes\Menu\Window.png")

        self.show_dialog(menu_play)

    def btn_config_click(self, param):
        self.menu_options = FormMenuOptions(self._master, 
        x= 400, 
        y= 100, 
        w= 400, 
        h= 300, 
        color_background = NEGRO, 
        color_border = VERDE, 
        active = True, 
        path_image = "Modulos\Assets\Imagenes\Menu\Window.png")

        self.show_dialog(self.menu_options)

    def btn_quit_click(self, param):
        self.exit = True