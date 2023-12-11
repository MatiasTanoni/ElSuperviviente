import sqlite3

# Path "Modules\Data\scores.db"

def crear_tabla(db_path):
    """
    Brief: Crea la tabla 'Tabla' en la base de datos si no existe.
        Esta función se conecta a la base de datos especificada y crea la tabla 'Tabla' si aún no existe.
        La tabla 'Tabla' tiene las columnas 'id_jugador' (clave primaria), 'nombre_jugador' y 'puntos_jugador'.
    Parámetros:
        - db_path (str): Ruta al archivo de la base de datos.
    """
    with sqlite3.connect(db_path) as conexion:
        try:
            sentencia = '''
                        CREATE TABLE IF NOT EXISTS Tabla       
                        (
                            id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_jugador TEXT,
                            puntos_jugador INTEGER
                        )
                        '''
            conexion.execute(sentencia)
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        except Exception as f:
            print(f"Error: {f}")

def insertar_datos(db_path, nombre_jugador, puntos_jugador):
    """
    Brief: Inserta datos del jugador en la tabla 'Tabla' de la base de datos.
        Esta función se conecta a la base de datos especificada e inserta datos del jugador en la
        tabla 'Match'. Los datos incluyen el nombre del jugador y la puntuación.
    Parámetros:
        - db_path (str): Ruta al archivo de la base de datos.
        - nombre_jugador (str): Nombre del jugador.
        - puntos_jugador (int): Puntuación del jugador.
    """
    with sqlite3.connect(db_path) as conexion:
        try:
            sentencia = f"INSERT INTO Tabla (nombre_jugador,  puntos_jugador) VALUES ('{nombre_jugador}', {puntos_jugador} )"
            conexion.execute(sentencia)
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        except Exception as f:
           print(f"Error: {f}") 

def obtener_top_puntaje(db_path):
    """
    Brief: Obtiene los tres puntajes más altos con nombres de la tabla 'Tabla' en la base de datos.
        Esta función se conecta a la base de datos especificada y realiza una consulta para obtener
        los tres puntajes más altos con los nombres correspondientes desde la tabla 'Tabla'.
    Parámetros:
        - db_path (str): Ruta al archivo de la base de datos.
    Retorno:
        list: Lista de tuplas que contienen nombres de jugadores y sus puntajes, ordenados por puntaje descendente.
    """
    with sqlite3.connect(db_path) as conexion:
        try:
            sentencia = "SELECT nombre_jugador, puntos_jugador FROM Tabla ORDER BY puntos_jugador DESC LIMIT 3"
            resultado = conexion.execute(sentencia).fetchall()

            return resultado
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        except Exception as f:
           print(f"Error: {f}") 