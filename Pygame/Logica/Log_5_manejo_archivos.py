import re
import json
from datetime import datetime

def leer_csv(path:str)->list:
    """Esta funcion lee un archivo csv recibido por el parametro path, elimina espacios
    vacios y realiza la separacion por medio de las comas.

    Args:
        path (str): Path que contiene la ruta al archivo

    Returns:
        list: Retorna una lista de listas. Cada linea del archivo sera una lista.
    """
    with open(path,"r", encoding="utf8") as archivo:  
        lista = []
        for linea in archivo:
            linea = linea.strip()        
            linea = re.split(",",linea)
            lista += [linea]

    return lista

# def crear_json(path_json: str) -> list:
#     """Crea un archivo json. Verifica si existe el archivo. Si no existe lo crea. 
#     Tambien inicializa una lista vacia.

#     Args:
#         path_json (str): ruta al archivo json

#     Returns:
#         list: lista vacia donde se ira completando con diccionarios.
#     """
    
#     estadisticas = []

#     try:
#         with open(path_json, "r"):
#             pass

#     except FileNotFoundError:

#         with open(path_json, "w") as archivo:  
#             json.dump(estadisticas, archivo, indent=4)  
#             print("El archivo resultados.json se ha creado satisfactoriamente")

#     return estadisticas

def crear_diccionario_estadisticas(jugador, puntaje)->dict:
    """Descripción: Crea el diccionario de las estadísticas. 

    Args:
        jugador (str): El nombre del jugador que gano.
        puntaje (str): El puntaje de cada jugador.

    Returns:
        dict: Diccionario con los datos finales para ser guardados.
    """
    estadistica = {
        "nombre_jugador" : jugador,
        "fecha_victoria":  datetime.now().strftime("%d/%m/%Y"),
        "puntaje_obtenido": puntaje
    }
    return estadistica

def verificar_existencia_archivo_json(path_json)->bool:
    """Descripción: Verifica que ya exista un archivo Json.

    Args:
        path_json (_type_): Ruta del archivo Json.

    Returns:
        bool: si hay existencia o no de un archivo Json.
    """
    existe = True
    try:
        with open(path_json, "r"):
            pass

    except FileNotFoundError:
    
        existe = False

    return existe

def guardar_resultados(pantalla:dict ,puntaje: int, jugador: str):#! PATH JSON
    """Descripcion: Guarda las estadisticas del jugador ganador

    Args:
        path_json (str): ruta al archivo json
        puntaje (int): es el puntaje del jugador ganador
        jugador (str): es el nombre del jugador ganador
    """
    
    nueva_estadistica = crear_diccionario_estadisticas(jugador, puntaje)
    existe_json = verificar_existencia_archivo_json(pantalla["path_json"])

    if existe_json == False:
        estadisticas = []
        
    else:
        with open(pantalla["path_json"], "r") as archivo:
            estadisticas = json.load(archivo)
        
    estadisticas.append(nueva_estadistica)
    
    with open(pantalla["path_json"], "w") as archivo: #aca se crea el Json     
        json.dump(estadisticas, archivo, indent=4)


#############################################

# NUEVA VERSION

# def crear_json(pantalla:dict, estadisticas:list) -> list:

#     with open(pantalla["path_json"], "w") as archivo:  
#         json.dump(estadisticas, archivo, indent=4)  
