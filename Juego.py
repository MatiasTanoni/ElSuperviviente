from Modulos.Niveles.nivel import Nivel
from Modulos.Gui.GUI_form_main import FormMain
from Modulos.Values.activos import *
from Modulos.Values.colores import *
from pygame.locals import *
import pygame as py
from pygame import mixer
import sys

class Juego(Nivel):
    def __init__(self, size):
        """
        Brief: Constructor de la clase que inicializa la instancia.
            Este constructor llama al constructor de la clase base con el tamaño especificado.
            Además, inicializa los atributos 'screen' y 'form_main' con valores predeterminados.
        Parámetros:
            - size: Tamaño de la ventana del juego.
        """
        super().__init__(size)
        self.establecer_imagen_fondo(r"Modulos\Assets\Imagenes\menu.png")
        self.form_main = FormMain(self.pantalla, 400, 50, 400, 400, NEGRO, VERDE, 5, True)
        

    def init(self):
        """
        Brief: Inicializa y ejecuta el bucle principal del juego.
            Este método inicializa la biblioteca Pygame y ejecuta el bucle principal del juego.
            Controla eventos, actualiza la lógica del juego y mantiene la ejecución hasta que
            se cumple una condición de salida. Luego, finaliza la ejecución y libera los recursos.
        """
        py.init()


        while self.correr_juego:
            self.clock.tick(self.FPS)
            events = py.event.get()
            for event in events:
                if event.type == QUIT:
                    py.quit()
                    sys.exit()

            if self.form_main.exit:
                self.correr_juego = False

            self.llenar_pantalla()
            self.form_main.actualizar(events)
            py.display.flip()
        py.quit()