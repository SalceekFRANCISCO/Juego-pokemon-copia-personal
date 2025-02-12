import pygame
# from Visuales import *
# from Logica.Consola_2_FG import *
# from Funciones_pygame.Visuales import *
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
                               pokebola, carta_1, carta_2, jugadores, 
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
    pantalla["reemplazo_nombre"] = reemplazo_boton
    # pantalla["boton_reinicio"] = boton_reinicio
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

def crear_diccionario_acciones(bandera,texto_pantalla):
    accion = {}
    accion["bandera"] = bandera
    accion["texto_pantalla"] = texto_pantalla

    return accion

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

############################# INTERACCION ########################
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

def crear_diccionario_texto(pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto):
    texto = {}
    texto["ventana"] = pantalla["ventana"]
    texto["texto_escrito"] = renderizar_mensaje((fuente[0],fuente[1]),texto_escrito,color_texto,color_fondo_texto)
    texto["posicion"] = posicion

    return texto

def renderizar_mensaje(fuente:tuple, mensaje: str, color_texto: tuple,color_fondo_texto):
    fuente_creada = crear_fuente(fuente[0],fuente[1])
    texto_definitivo = renderizar_texto(fuente_creada,mensaje,color_texto,color_fondo_texto)

    return texto_definitivo

def crear_fuente(tipo_fuente: str, tamaño: int):
    """
    Crea una fuente de texto.

    Args:
        tipo_fuente (str): Nombre de la fuente.
        tamaño (int): Tamaño de la fuente.

    Returns:
        Font: Objeto de fuente creado.
    """
    fuente = pygame.font.SysFont(tipo_fuente,tamaño)
    return fuente

def renderizar_texto(fuente_creada: str, mensaje: str, color_texto: tuple, color_fondo_texto=None):
    """
    Renderiza un texto con la fuente, colores de texto y fondo.

    Args:
        fuente_creada (Font): Objeto de fuente.
        mensaje (str): Texto a renderizar.
        color_texto (tuple): Color del texto.
        color_fondo_texto (tuple): Color del fondo del texto.

    Returns:
        Surface: Superficie con el texto renderizado.
    """
    if color_fondo_texto != None:
        texto = fuente_creada.render(mensaje,False,color_texto,color_fondo_texto)
    else:
        texto = fuente_creada.render(mensaje,False,color_texto)

    return texto

def dibujar_solo_texto(texto:dict):
    """Muestra solo texto en la ventana.

    Args:
        texto (dict): Diccionario con datos del texto.
    """
    texto["ventana"].blit(texto["texto_escrito"],texto["posicion"])

def inicializar_ventana():
    ANCHO_VENTANA = 1300
    ALTO_VENTANA = 700

    pygame.init()
    pygame.mixer.init()

    ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

    pygame.display.set_caption("Pokemon Cards")

    icono = pygame.image.load("Poke_fotos\pokebola.png")
    pygame.display.set_icon(icono)

    return ventana

def crear_matriz_jerarquias():

    matriz_jerarquias_mezclada = [["Agua", ("Fuego", "Tierra")],
                    [("Electricidad", "Fuego"),"Tierra"],
                    ["Aire",("Tierra","Agua")],
                    [("Aire", "Hielo"),"Fuego"],
                    ["Electricidad",("Agua", "Hielo")], 
                    [("Normal", "Fuego"),"Psíquico"],
                    ["Normal",("Agua", "Aire")],
                    [("Tierra", "Aire"),"Hielo"]]

    return matriz_jerarquias_mezclada


#region nuevas funciones para escribir por pantalla
############################################################# 
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

def guardar_texto(pantalla:dict,fuente:tuple,color_texto,boton_nombre:dict,posicion_texto: tuple,evento,color_fondo_texto):
    texto_pantalla = ""
    nombre_final = escribir_teclado(boton_nombre,evento)

    texto_pantalla = crear_diccionario_texto(pantalla,fuente,nombre_final,color_texto,posicion_texto,color_fondo_texto)
            
    return texto_pantalla

#endregion