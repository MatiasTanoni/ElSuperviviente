import pygame as py
from Modulos.Values.colores import *

class Nivel:
    def __init__(self,tamano):
        py.mixer.init()
        self.establecer_icono("Modulos\Assets\Imagenes\icono.png")
        self.establecer_fps(18)
        self.establecer_titulo("Juego")
        self.correr_juego = True
        self.tamano = tamano
        self.pantalla = py.display.set_mode(self.tamano)
        self.clock = py.time.Clock()
        self.DEBUG = False
        self.tiempo_inicial = py.time.get_ticks() + 300 * 1000
        self.tiempo_restante = self.tiempo_inicial
        self.completado = False
        self.pausa = False


    def reanudar_juego(self):
        self.pausa = False

    def pausar_juego(self):
        self.pausa = True

    def establecer_titulo(self,titulo):
        """
        Brief:Establece el título de la ventana de la aplicación.
        Parametros: titulo: Nuevo título de la ventana.
        """
        self.titulo = py.display.set_caption(titulo)

    def establecer_icono(self, icono):
        """
        Brief: Establece el icono de la ventana de la aplicación.
        Parametros: -icono: Ruta al archivo de la imagen del icono.
        """
        self.icono = py.image.load(icono)
        py.display.set_icon(self.icono)
    
    def establecer_fps(self, FPS):
        """
        Brief: Establece FPS en la pantalla.
        Parámetros:
            -FPS(int): Cantidad de FPS ingresados.
        """
        self.FPS = FPS

    def establecer_musica(self, musica):
        """
        Brief: Establece y reproduce la música de fondo.
        Crea un objeto de sonido con la música proporcionada, ajusta el volumen y la reproduce.
        Parámetros:
            - musica (str): Ruta al archivo de música.
        """
        self.musica = py.mixer.Sound(musica)
        self.musica.set_volume(0.2)
        self.reproducir_musica()

    def establecer_volumen(self, volumen):
        """
        Brief: Establece el volumen de la música de fondo.
        Utiliza la función 'set_volume()' para ajustar el volumen de la música.
        Parámetros:
            - volumen (float): Valor entre 0.0 y 1.0 que representa el volumen deseado.
        """
        self.musica.set_volume(volumen)

    def reproducir_musica(self):
        """
        Brief: Reproduce la música de fondo en bucle.
        Utiliza la función 'play()' para iniciar la reproducción de la música en bucle.
        """
        self.musica.play(-1)

    def detener_musica(self):
        """
        Brief: Detiene la reproducción de la música.
        Utiliza la función 'stop()' para detener la reproducción de la música actual.
        """
        self.musica.stop()

    def establecer_imagen_fondo(self, fondo):
        """
        Brief: Establece una imagen como fondo de la pantalla y la escala al tamaño especificado.
        Carga la imagen proporcionada, la escala al tamaño de la pantalla y la asigna como fondo.
        Parámetros:- fondo (str): Ruta al archivo de imagen a utilizar como fondo.
        """
        self.imagen_fondo = py.image.load(fondo)
        self.imagen_fondo = py.transform.scale(self.imagen_fondo, self.tamano)

    def llenar_pantalla(self, color=None):
        """
        Brief: Llena la pantalla con un color específico o una imagen de fondo.
        Si se proporciona un color, llena la pantalla con ese color. De lo contrario, utiliza
        una imagen de fondo para llenar la pantalla.
        Parámetros:
            - color (tuple or None): Color para llenar la pantalla o None para usar la imagen de fondo.
        """
        if color is not None:
            self.pantalla.fill(color)
        else:
            self.pantalla.blit(self.imagen_fondo, (0, 0))

    def actualizar(self,lista_eventos):
        """
        Brief: Actualiza el estado del juego según la lista de eventos proporcionada.
        Recorre la lista de eventos y, si se detecta que la tecla TAB ha sido presionada,
        cambia el modo de debug llamando a la función 'cambiar_modo'.
        Parámetros:
            - lista_eventos (list): Lista de eventos capturados por Pygame.
        """
        for evento in lista_eventos:
            if evento.type == py.KEYDOWN:
                if evento.key == py.K_TAB:
                    self.cambiar_modo()
            self.llenar_pantalla()

    def cambiar_modo(self):
        """
        Brief: Cambia el modo de debug entre activado y desactivado.
            Modifica el valor del atributo DEBUG de la instancia, alternando entre True y False.
        """
        self.DEBUG = not self.DEBUG
    
    def obtener_modo(self):
        """
        Brief: Obtiene el modo de debug.
                Retorna el valor del atributo DEBUG de la instancia.
        Retorno:
            - bool: Valor del modo de debug (True o False).
        """
        return self.DEBUG

    def hitboxes(self):
        """
        Brief: Dibuja los contornos de las hitboxes en la pantalla.
        Si el juego está en modo debug, dibuja los contornos de las hitboxes de plataformas, personaje,
        enemigos, bombas, objetos que caen, items, proyectiles y el jefe en la pantalla.
        Parametros:-self
        """

        if self.obtener_modo():
            for pl in self.plataformas:
                py.draw.rect(self.pantalla, ROJO, pl.rectangulo, 2)
            py.draw.rect(self.pantalla, ROJO, self.personaje.rectangulo, 2)
            for enemigo in self.enemigos:
                py.draw.rect(self.pantalla, ROJO, enemigo.rectangulo, 2)
            for bomba in self.bombitas:
                py.draw.rect(self.pantalla, ROJO, bomba.rectangulo, 2)
            for obj in self.objetos_caen:
                py.draw.rect(self.pantalla, ROJO, obj.rectangulo, 2)
            for item in self.items:
                py.draw.rect(self.pantalla, LIMA, item.rectangulo, 2)
            for proyectil in self.personaje.lista_proyectiles:
                py.draw.rect(self.pantalla, ROJO, proyectil.rectangulo, 2)
            try:
                py.draw.rect(self.pantalla, ROJO, self.jefe.rectangulo, 2)
            except AttributeError:
                pass

    def mostrar_score(self, texto):
        """
        Brief: Muestra el puntaje en la pantalla.  
                Utiliza la biblioteca Pygame para renderizar y mostrar el puntaje en la posición especificada.
        Parámetros:
            - texto (str): Puntaje a ser mostrado en la pantalla.
        """
        fuente = py.font.SysFont('Arial Black', 30)
        texto = fuente.render(f"score: {texto}", True, BLANCO)
        self.pantalla.blit(texto, (30,5))
    
    def mostrar_tiempo(self): 
        """
        Brief: Muestra el tiempo restante en la pantalla en formato minutos:segundos.
        Actualiza el tiempo restante basado en el tiempo actual y lo muestra en la pantalla.
        Parametros:
            - self
        """
        
        tiempo_actual = py.time.get_ticks()
        self.tiempo_restante = max(self.tiempo_inicial - tiempo_actual,0)
        tiempo_seconds = self.tiempo_restante // 1000
        minutos = tiempo_seconds // 60
        segundos = tiempo_seconds % 60
        mensaje = f"{minutos:.0f}:{segundos}"
        fuente = py.font.SysFont("Arial Black", 38)
        mensaje = fuente.render(mensaje, 0, BLANCO)
        self.pantalla.blit(mensaje, (522,0))

    def aplicar_mensaje(self, mensaje: str, posicion_x: int, posicion_y: int, color: tuple, tamaño: int, fuente: str = ""):
        """
        Brief: 
            Aplica un mensaje creado a la pantalla.
        Parametros:
            mensaje:str = El mensaje.
            posicion_x:int = posicion en el eje x.
            posicion_y:int = posicion en el eje y.
            color:tuple = Un color especifico.
            tamaño:int = El tamaño del mensaje.
            fuente:str = La fuente del mensaje.
        Retorno:
        """
        mi_fuente = py.font.SysFont(fuente, tamaño)
        mensaje = mi_fuente.render(mensaje, 0, color)

        self.pantalla.blit(mensaje, (posicion_x, posicion_y))
