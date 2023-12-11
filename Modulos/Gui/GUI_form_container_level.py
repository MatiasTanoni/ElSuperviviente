from Modulos.Data.Data import *
from Modulos.Gui.GUI_button_image import *
from Modulos.Gui.GUI_form import *
from Modulos.Gui.GUI_form_menu_pause import FormMenuPause
from Modulos.Values.colores import *

class FormContainerLevel(Form):
    def __init__(self, screen: pygame.Surface, level, name):
        super().__init__(screen, 0, 0, screen.get_width(), screen.get_height(), color_background = AZUL_MARINO)
        level.screen = self._slave
        self.nivel = level
        self.flag_music_play = True
        self.nombre_jugador = name

        self._btn_home = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 50,
                        y = self._h - 40,
                        w = 30,
                        h = 30,
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image = "Modulos\Assets\Imagenes\Menu\home.png") 
        
        self._btn_pause = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 110,
                        y = self._h - 40,
                        w = 30,
                        h = 30,
                        onclick = self.btn_pause_click,
                        onclick_param = "",
                        path_image = "Modulos\Assets\Imagenes\Menu\pause.png") 
        
        self._btn_sound = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 170,
                        y = self._h - 40,
                        w = 30,
                        h = 30,
                        onclick = self.btn_sound_click,
                        onclick_param = "",
                        path_image = "Modulos\Assets\Imagenes\Menu\sound.png") 
        
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_pause)
        self.lista_widgets.append(self._btn_sound)

    def render(self):
        self._slave.fill(self._color_background)

    def actualizar(self, events):                                           
        if not self.nivel.completado and self.nivel.personaje.vidas > 0 and self.nivel.tiempo_restante != 0:
            if self.verificar_dialog_result():
                if self.active:
                    self.draw()
                    self.render()
                    for widget in self.lista_widgets: 
                        widget.actualizar(events)
            else:
                self.hijo.actualizar(events)
        else:
            self.nivel.detener_musica()
            if self.nivel.completado:
                insertar_datos("Modulos\Data\puntaje.db", self.nombre_jugador, self.nivel.personaje.puntos)
            del self.nivel
            self.end_dialog()

    def btn_home_click(self, param):
        self.nivel.detener_musica()
        del self.nivel
        self.end_dialog()
    
    def btn_sound_click(self, param):
        if self.flag_music_play:
            self.nivel.detener_musica()
        else:
            self.nivel.reproducir_musica()
        
        self.flag_music_play = not self.flag_music_play

    def btn_pause_click(self, param):
        self.nivel.pausar_juego()
        self.nivel.detener_musica()

        menu_pause = FormMenuPause(self._master, 
        x= 400, 
        y= 100, 
        w= 400, 
        h= 300, 
        color_background = BLANCO, 
        color_border = BLANCO, 
        active = True,
        level= self.nivel, 
        path_image = "Modulos\Assets\Imagenes\Menu\Window.png")
    
        self.show_dialog(menu_pause)

        

          
 