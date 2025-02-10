import pygame
from Funciones_pygame.Visuales_copy import *
# from Funciones_pygame.Dicc_interaccion import *

def crear_cuadrados(ventana, color, posicion: tuple, dimensiones: tuple) -> dict:
    """
    Crea un diccionario que representa un cuadrado en Pygame.

    Args:
        ventana: Superficie de Pygame donde se dibujará el cuadrado.
        color: Color del cuadrado en formato RGB.
        posicion (tuple): Coordenadas (x, y) del cuadrado.
        dimensiones (tuple): Ancho y alto del cuadrado.

    Returns:
        dict: Diccionario con los datos del cuadrado.
    """

    cuadrado = {}
    cuadrado["ventana"]= ventana
    cuadrado["color_actual"]= color
    cuadrado["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])

    return cuadrado

def crear_input(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,texto_del_boton=None,texto_escritura=None) -> dict:
    """
    Crea un diccionario que representa un campo de entrada (input) en Pygame.

    Args:
        ventana: Superficie de Pygame donde se dibujará el campo de entrada.
        fuente (tuple): Tipo y tamaño de fuente a utilizar (nombre, tamaño).
        colores (dict): Diccionario con los colores disponibles.
        posicion (tuple): Coordenadas (x, y) del campo de entrada.
        dimensiones (tuple): Ancho y alto del campo de entrada.
        texto_del_boton (str): Texto inicial del campo de entrada.

    Returns:
        dict: Diccionario con los datos del campo de entrada.
    """
    input = {}
    input["ventana"] = ventana
    input["fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
    input["color_activo"] = colores["dorado"]
    input["color_inactivo"] = colores["blanco"]
    input["activo"] = False
    input["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
    input["color_actual"] = colores["blanco"]

    if texto_del_boton != None:
        input["texto"] = texto_del_boton # la llave tiene que llamarse texto_del_boton

    elif texto_escritura != None:
        input["texto_escritura"] = texto_escritura

    return input
           
def crear_colores(NEGRO, ROJO, AZUL, AZUL_CLARO, VERDE, BLANCO, DORADO, GRIS) -> dict:
    """
    Crea un diccionario con colores definidos.

    Args:
        NEGRO: Color negro en formato RGB.
        ROJO: Color rojo en formato RGB.
        AZUL: Color azul en formato RGB.
        AZUL_CLARO: Color azul claro en formato RGB.
        VERDE: Color verde en formato RGB.
        BLANCO: Color blanco en formato RGB.
        DORADO: Color dorado en formato RGB.
        GRIS: Color gris en formato RGB.

    Returns:
        dict: Diccionario con los colores asociados a sus nombres.
    """    
    
    colores = {}
    colores["negro"] = NEGRO
    colores["rojo"] = ROJO
    colores["azul"] = AZUL
    colores["azul_claro"] = AZUL_CLARO
    colores["verde"] = VERDE
    colores["blanco"] = BLANCO
    colores["dorado"] = DORADO
    colores["gris"] = GRIS

    return colores

def crear_diccionario_pantalla(ventana, GRIS, lista_cuadrados, boton_jugar, reemplazo_boton, 
                               boton_reinicio, pokebola, carta_1, carta_2, jugadores, 
                               path_json, path_csv, boton_ganador_partida,atributo,boton_nombre_uno,boton_nombre_dos) -> dict:
    """
    Crea un diccionario que almacena los datos principales de la pantalla.

    Args:
        ventana: Superficie de Pygame donde se dibujarán los elementos.
        GRIS: Color de fondo de la ventana.
        lista_cuadrados (list): Lista de cuadrados en la pantalla.
        boton_jugar: Botón de inicio del juego.
        reemplazo_boton: Botón de reemplazo para alguna acción específica.
        boton_reinicio: Botón para reiniciar el juego.
        pokebola: Imagen o referencia a la pokebola.
        carta_1, carta_2: Cartas asociadas a los jugadores.
        jugadores (list): Lista de jugadores (jugador 1 y jugador 2).
        path_json (str): Ruta al archivo JSON relacionado.
        path_csv (str): Ruta al archivo CSV relacionado.

    Returns:
        dict: Diccionario con los datos de la pantalla.
    """
    pantalla = {}
    pantalla["ventana"] = ventana
    pantalla["color_ventana"] = GRIS
    pantalla["lista_cuadrados"] = lista_cuadrados
    pantalla["boton_jugar"] = boton_jugar
    pantalla["reemplazo_boton"] = reemplazo_boton
    pantalla["boton_reinicio"] = boton_reinicio
    pantalla["pokebola"] = pokebola
    pantalla["carta_1"] = carta_1
    pantalla["carta_2"] = carta_2
    pantalla["jugador_1"] = jugadores[0]
    pantalla["jugador_2"] = jugadores[1]
    pantalla["path_json"] = path_json
    pantalla["path_csv"] = path_csv
    pantalla["ganador_partida"] = boton_ganador_partida
    pantalla["atributo"] = atributo
    pantalla["boton_nombre_uno"] = boton_nombre_uno
    pantalla["boton_nombre_dos"] = boton_nombre_dos

    return pantalla

def crear_diccionario_listas() -> dict:
    """
    Crea un diccionario para almacenar listas relacionadas con el juego.

    Returns:
        dict: Diccionario con listas vacías para uso en el juego.
    """
    listas = {}
    listas["lista_jugador_uno"] = [] 
    listas["lista_jugador_dos"] = [] 
    listas["cartas_jugadores"] = [] 
    listas["lista_cartas"] = [] 
    listas["cartas_meza"] = [] 

    return listas

def crear_diccionario_texto(pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto):
    texto = {}
    texto["ventana"] = pantalla["ventana"]
    texto["texto_escrito"] = renderizar_mensaje((fuente[0],fuente[1]),texto_escrito,color_texto,color_fondo_texto)
    texto["posicion"] = posicion

    return texto

def crear_diccionario_imagen(ventana, path, coordenadas, dimensiones)->dict:
    """
    Crea una imagen escalada y la asocia a una ventana.

    Args:
        ventana (Surface): Superficie donde se dibujará la imagen.
        path (str): Ruta de la imagen.
        coordenadas (tuple): Coordenadas (x, y) de la imagen.
        dimensiones (tuple): Escala (ancho, alto) de la imagen.

    Returns:
        dict: Diccionario con datos de la imagen.
    """
    imagen = {}
    imagen_cargada = cargar_imagenes(path,dimensiones)
    imagen["imagen_final"] = imagen_cargada 
    imagen["ventana"] = ventana 
    imagen["coordenadas"] = coordenadas 

    return imagen



############################# INTERACCION ########################
def guardar_texto(pantalla:dict,fuente:tuple,color_texto,boton_nombre:dict,posicion_texto: tuple,evento,color_fondo_texto):
    texto_pantalla = ""
    nombre_final = escribir_teclado(boton_nombre,evento)

    texto_pantalla = crear_diccionario_texto(pantalla,fuente,nombre_final,color_texto,posicion_texto,color_fondo_texto)
            
    return texto_pantalla

def escribir_teclado(input_1, evento):
    texto_final = ""
    if input_1["activo"]:
        if evento.key == pygame.K_BACKSPACE:
            input_1["texto_escritura"] = input_1["texto_escritura"][:-1]
            texto_final = input_1["texto_escritura"]

        elif evento.key == pygame.K_RCTRL:
            texto_final = ""
            input_1["texto_escritura"] = ""

        elif evento.key == pygame.K_RETURN:
            input_1["activo"] = False
            input_1["color_actual"] = input_1["color_inactivo"]
            texto_final = input_1["texto_escritura"] 
        else:
            input_1["texto_escritura"] += evento.unicode
            texto_final = input_1["texto_escritura"]

    return texto_final

def cambio_color(input_1):
    """
    Cambia el color de un campo de entrada basado en su estado (activo/inactivo).

    Args:
        input_1 (dict): Diccionario del campo de entrada.
    """
    input_1["activo"] = not input_1["activo"]
    if input_1["activo"]:
        input_1["color_actual"] = input_1["color_activo"] 
    else:
        input_1["color_actual"] = input_1["color_inactivo"]

def inicializar_ventana():
    ANCHO_VENTANA = 1300
    ALTO_VENTANA = 700

    pygame.init()
    pygame.mixer.init()

    ventana = pygame.display.set_mode(ANCHO_VENTANA,ALTO_VENTANA)

    pygame.display.set_caption("Pokemon Cards")

    return ventana

#region musica
############################################################# 
def reproducir_musica (musica: str, repeticion: int, volumen: float):
    """Descripción: Reproduce la musica que se le pasa por parametro.

    Args:
        musica (str): path del archivo
        repeticion (int): Cuantas veces va a repetirse la cancion
        volumen (float): el volumen de la cancion
    """
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(repeticion)
    pygame.mixer.music.set_volume(volumen)

# Si repeticion = 0: la pista se reproduce una sola vez.
# Si repeticion = 1: la pista se reproduce una vez más después de terminar, es decir, en total se reproduce dos veces.
# Si repeticion = -1: la pista se reproduce en bucle infinito.
#endregion
