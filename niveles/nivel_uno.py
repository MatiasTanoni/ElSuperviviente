import pygame as py
from caracteres.classItem import Item
from caracteres.classCaenObjetos import CaenObjetos
from caracteres.classPersonaje import Personaje
from caracteres.classEnemigo import Enemigo
from caracteres.classPlataformas import Plataforma
from caracteres.classTrampas import Trampas
from niveles.nivel import Nivel

class NivelUno(Nivel):
    def __init__(self,tamano):
        super().__init__(tamano)
        self.establecer_imagen_fondo("imagenes\\background.png")
        self.personaje = Personaje((70,100),(900,460),10)
        self.estado = "sin completar"
        self.bombitas = self.crear_bombitas()
        self.plataformas = self.crear_plataforma()
        self.objetos_caen = self.crear_objetos_que_caen()
        self.items = self.crear_items()
        self.enemigos = self.crear_enemigos()
        self.volumen = 0.1

    def crear_plataforma(self):
        """
        Brief: Crea y devuelve una lista de objetos de tipo Plataforma.
        Retorno:plataformas: Lista de objetos Plataforma.
        """
        plataformas = []

        plataforma_principal = Plataforma((1200,84),(0,565),"sin imagen")
        plataforma_a = Plataforma((440,40),(0,325))
        plataforma_b = Plataforma((500,40),(700,245))  
        plataforma_c = Plataforma((500,40),(600,420))
        plataforma_d = Plataforma((600,55),(0,0))
        plataforma_e = Plataforma((600,55),(600,0))

        plataformas.append(plataforma_a)
        plataformas.append(plataforma_b)
        plataformas.append(plataforma_c)
        plataformas.append(plataforma_d)
        plataformas.append(plataforma_e)
        plataformas.append(plataforma_principal)

        return plataformas
    
    def crear_enemigos(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo Enemigo.
        Retorno:enemigos: Lista de objetos Enemigo.
        """
        enemigos = []

        enemigo_a = Enemigo((70,100),(0,500),(200,465))
        enemigo_b = Enemigo((70,100),(0,300),(300,226))

        enemigos.append(enemigo_a)
        enemigos.append(enemigo_b)

        return enemigos


    def crear_bombitas(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo Trampas (bombitas).
        Retorno:bombitas: Lista de objetos Trampas.
        """
        bombitas = []

        bombita_a = Trampas((35,35),(700,530))
        bombita_b =  Trampas((35,35),(770,210))

        bombitas.append(bombita_a)
        bombitas.append(bombita_b)

        return bombitas

    def crear_objetos_que_caen(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo CaenObjetos.
        Retorno:objetos: Lista de objetos.
        """
        objetos = []

        objeto_a = CaenObjetos((35,35),"fuego",(200,2),12)
        objeto_b = CaenObjetos((35,35),"fuego",(150,2),12)
        objeto_c = CaenObjetos((35,35),"fuego",(90,2),12)
        objeto_d = CaenObjetos((35,35),"fuego",(300,2),12)
        objeto_e = CaenObjetos((35,35),"",(451,2),12)
        objeto_f = CaenObjetos((35,35),"",(451,2),12)

        objetos.append(objeto_a)
        objetos.append(objeto_b)
        objetos.append(objeto_c)
        objetos.append(objeto_d)
        objetos.append(objeto_e)
        objetos.append(objeto_f)

        return objetos
    
    def crear_items(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo Item.
        Retorno:items: Lista de objetos item.
        """
        items = []

        item_a = Item((25,45),"agua",(200,280))
        item_b = Item((35,35),"comida",(150,530))
        item_c = Item((35,35),"comida",(1050,530))
        item_d = Item((35,35),"comida",(1000,210))
        item_e = Item((25,45),"agua",(1050,200))
        item_f = Item((70,110),"puerta",(1132,138))

        items.append(item_a)
        items.append(item_b)
        items.append(item_c)
        items.append(item_d)
        items.append(item_e)
        items.append(item_f)

        return items

    def actualizar(self,evento):
        """
        Brief:Actualiza la pantalla del juego.
        Parametros: evento: Evento del juego.
        """
        super().actualizar(evento)
        self.llenar_pantalla()
        self.blitear_plataformas()
        self.personaje.actualizar(self.pantalla,self.plataformas,self.enemigos,self.bombitas,self.objetos_caen,self.items)
        self.blitear_objetos_que_caen()
        self.blitear_items()
        self.blitear_bombitas()
        for enemigo in self.enemigos:
            enemigo.actualizar(self.pantalla)
        self.hitboxes()
        self.mostrar_score(self.personaje.puntos)
        self.mostrar_tiempo()

    def blitear_plataformas(self):
        """
        Realiza el blit de las plataformas en la pantalla.
        """
        for plataforma in self.plataformas:
            plataforma.blit(self.pantalla)
    
    def blitear_items(self):
        """
        Brief: Realiza el blit de los items en la pantalla.
        """
        for item in self.items:
            item.blit(self.pantalla)
    
    def blitear_objetos_que_caen(self):
        """
        Brief:Realiza el blit de los objetos que caen en la pantalla, moviéndolos hacia abajo.
        """
        for objeto_que_cae in self.objetos_caen:
            objeto_que_cae.mover_abajo()
            objeto_que_cae.blit(self.pantalla)

    def blitear_bombitas(self):
        """
        Brief:Realiza el blit de las bombitas en la pantalla.
        """
        for bombita in self.bombitas:
            bombita.blit(self.pantalla)

        
