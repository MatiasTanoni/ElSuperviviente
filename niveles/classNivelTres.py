from caracteres.ClassJefeFinal import Jefe
from caracteres.classItem import Item
from caracteres.classCaenObjetos import CaenObjetos
from caracteres.classPersonaje import Personaje
from caracteres.classEnemigo import Enemigo
from caracteres.classPlataformas import Plataforma
from caracteres.classTrampas import Trampas
from niveles.nivel import Nivel

class NivelTres(Nivel):
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
        self.jefe = self.crear_jefe()

    def crear_plataforma(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo Plataforma.
        Retorno:plataformas: Lista de objetos Plataforma.
        """
        plataformas = []

        plataforma_principal = Plataforma((1200,84),(0,565),"sin imagen")

        plataforma_a = Plataforma((500,40),(350,420))
        plataforma_b = Plataforma((200,20),(950,345))  
        plataforma_c = Plataforma((200,20),(50,345))
        plataforma_f = Plataforma((350,30),(425,210))

        plataforma_d = Plataforma((600,55),(0,0))
        plataforma_e = Plataforma((600,55),(600,0))

        plataformas.append(plataforma_a)
        plataformas.append(plataforma_b)
        plataformas.append(plataforma_c)
        plataformas.append(plataforma_d)
        plataformas.append(plataforma_e)
        plataformas.append(plataforma_f)
        plataformas.append(plataforma_principal)

        return plataformas
    
    def crear_jefe(self):
        """
        Brief:Crea y devuelve un objeto de tipo Jefe.
        Retorno:enemigos: Objeto Jefe.
        """
        enemigo_boss = Jefe((90,120),(420,700),(420,93),10)
        return enemigo_boss

    def crear_enemigos(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo Enemigo.
        Retorno:enemigos:Lista de objetos Enemigo.
        """
        enemigos = []

        enemigo_a = Enemigo((70,100),(0,500),(50,465),7)
        enemigo_b = Enemigo((70,100),(360,770),(360,320),7)
        enemigo_c = Enemigo((70,100),(50,120),(50,245),7)

        enemigos.append(enemigo_a)
        enemigos.append(enemigo_b)
        enemigos.append(enemigo_c)

        return enemigos


    def crear_bombitas(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo Trampas (bombitas).
        Retorno:bombitas: Lista de objetos Trampas.
        """
        bombitas = []

        bombita_a = Trampas((35,35),(155,530))
        bombita_b =  Trampas((35,35),(1000,310))
        bombita_c =  Trampas((35,35),(1005,530))
        bombita_d =  Trampas((30,30),(550,390))

        bombitas.append(bombita_a)
        bombitas.append(bombita_b)
        bombitas.append(bombita_c)
        bombitas.append(bombita_d)

        return bombitas

    def crear_objetos_que_caen(self):
        """
        Brief:Crea y devuelve una lista de objetos de tipo CaenObjetos.
        Retorno:objetos: Lista de objetos CaenObjetos.
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
        Retorno:items: Lista de objetos Item.
        """
        items = []

        item_a = Item((25,45),"agua",(1130,518))
        item_b = Item((35,35),"comida",(100,530))
        item_c = Item((35,35),"comida",(1090,310))
        item_d = Item((35,35),"comida",(500,175))
        item_e = Item((25,45),"agua",(80,300))
        item_f = Item((70,110),"puerta",(565,103))
        item_g = Item((25,45),"agua",(500,375))
        item_h = Item((35,35),"comida",(700,385))

        items.append(item_a)
        items.append(item_b)
        items.append(item_c)
        items.append(item_d)
        items.append(item_e)
        items.append(item_f)
        items.append(item_g)
        items.append(item_h)

        return items

    def actualizar(self,evento):
        """
        Brief:Actualiza la pantalla del juego.
        Parametros:evento: Evento del juego.
        """
        super().actualizar(evento)
        self.llenar_pantalla()
        self.blitear_plataformas()
        self.personaje.actualizar(self.pantalla,self.plataformas,self.enemigos,self.bombitas,self.objetos_caen,self.items,self.jefe)
        self.blitear_objetos_que_caen()
        self.blitear_items()
        self.blitear_bombitas()
        if self.jefe:
            self.jefe.actualizar(self.pantalla)
            if self.jefe.vidas == 0:
                del self.jefe
                self.jefe = None
        for enemigo in self.enemigos:
            enemigo.actualizar(self.pantalla)
        self.hitboxes()
        self.mostrar_score(self.personaje.puntos)
        self.mostrar_tiempo()

    def blitear_plataformas(self):
        """
        Brief:Realiza el blit de las plataformas en la pantalla.
        """
        for plataforma in self.plataformas:
            plataforma.blit(self.pantalla)
    
    def blitear_items(self):
        """
        Brief:Realiza el blit de los items en la pantalla.
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
    
    def blitear_jefe(self):
        """
        Brief:Realiza el blit del jefe en la pantalla.
        """
        self.jefe.blit(self.pantalla)

        
