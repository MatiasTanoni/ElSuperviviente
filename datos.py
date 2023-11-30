import sqlite3

# Path "Modules\Data\scores.db"

def crear_tabla_de_nivel(path):
    """
    Brief: Crea la tabla 'Tabla' en la base de datos si no existe.
        Esta función se conecta a la base de datos especificada y crea la tabla 'Tabla' si aún no existe.
    Parámetros:
        - path (str): Ruta al archivo de la base de datos.
    """
    with sqlite3.connect(path) as coneccion:
        try:
            sentencia = '''
                        CREATE TABLE IF NOT EXISTS Tabla       
                        (
                            indice_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_jugador TEXT,
                            puntuacion_jugador INTEGER
                        )
                        '''
            coneccion.execute(sentencia)
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")

def inserta_datos_jugador(path, nombre_jugador, puntos_jugador):
    """
    Brief: Inserta datos del jugador en la tabla 'Tabla' de la base de datos.
            Esta función se conecta a la base de datos especificada e inserta datos del jugador en la
            tabla 'Tabla'. Los datos incluyen el nombre del jugador y la puntuación.
    Parámetros:
        - path (str): Ruta al archivo de la base de datos.
        - nombre_jugador (str): Nombre del jugador.
        - puntos_jugador (int): Puntuación del jugador.
    """
    with sqlite3.connect(path) as coneccion:
        try:
            sentencia = f"INSERT INTO Tabla (nombre_jugador, puntuacion_jugador) VALUES ('{nombre_jugador}', {puntos_jugador})"
            coneccion.execute(sentencia)
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")

def obtener_top_puntajes(path):
    """
    Brief: Obtiene los tres puntajes más altos con nombres de la tabla 'Tabla' en la base de datos.
        Esta función se conecta a la base de datos especificada y realiza una consulta para obtener
        el puntaje más alto con el nombre correspondiente desde la tabla 'Tabla'.
    Parámetros:
        - path (str): Ruta al archivo de la base de datos.
    Retorno:
        -result:contiene el nombre del jugador y su puntaje.
    """
    with sqlite3.connect(path) as coneccion:
        try:
            sentence = "SELECT nombre_jugador, puntuacion_jugador FROM Tabla ORDER BY puntuacion_jugador DESC LIMIT 1"
            result = coneccion.execute(sentence).fetchall()

            return result
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
