import pygame
from Funciones_pygame.Diccionarios import *

def inicializar_elementos_ventana()->list:
    """Descripción: Carga los elementos de la ventana principal.

    Returns:
        list: Elementos de la ventana principal
    """
    
    ANCHO_VENTANA = 1300
    ALTO_VENTANA = 700
    lista = []

    pygame.init()
    pygame.mixer.init()

    ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

    pygame.display.set_caption("Pokemon Cards")

    icono = cargar_imagen("Poke_fotos\pokebola.png")
    pygame.display.set_icon(icono)

    fondo = cargar_imagenes(r"Poke_fotos\fondo_pikachu.png",(ANCHO_VENTANA, ALTO_VENTANA))

    fondo_2 = cargar_imagenes(r"Poke_fotos\paisaje_pokimon.png",(ANCHO_VENTANA, ALTO_VENTANA))

    lista.append(ventana)
    lista.append(fondo)
    lista.append(fondo_2)

    return lista

def crear_matriz_jerarquias()-> list[list]:
    """Descripción:

    Returns:
        list[list]: _description_
    """

    matriz_jerarquias_mezclada = [["Agua", ("Fuego", "Tierra")],
                    [("Electricidad", "Fuego"),"Tierra"],
                    ["Aire",("Tierra","Agua")],
                    [("Aire", "Hielo"),"Fuego"],
                    ["Electricidad",("Agua", "Hielo")], 
                    [("Normal", "Fuego"),"Psíquico"],
                    ["Normal",("Agua", "Aire")],
                    [("Tierra", "Aire"),"Hielo"]]

    return matriz_jerarquias_mezclada

def escribir_teclado(boton:dict, evento):
    """Descripción: Permite escribir por teclado.

    Args:
        boton (dict): Diccioanrio donde se guardan los datos.
        evento (_type_): evento que se produzca.
    """
    if boton["activo"]:
        if evento.key == pygame.K_BACKSPACE:
            boton["texto"] = boton["texto"][:-1]

        elif evento.key == pygame.K_RCTRL:
            boton["texto"] = ""

        elif evento.key == pygame.K_RETURN:
            boton["activo"] = False
            boton["color_actual"] = boton["color_inactivo"]

        else:
            if len(boton["texto"]) < 16:
                boton["texto"] += evento.unicode

def cambio_color(boton:dict):
    """
    Descripción: Cambia el color de un campo de entrada basado en su estado (activo/inactivo).

    Args:
        boton (dict): Diccionario del campo de entrada.
    """
    boton["activo"] = not boton["activo"]

    if boton["activo"]:
        boton["color_actual"] = boton["color_activo"] 
    else:
        boton["color_actual"] = boton["color_inactivo"]

def detectar_cambio_color(lista:list,evento):
    """Descripción: Detecta la acción de cambiar de color.

    Args:
        lista (list): lista de botones
        evento (): evento capturado
    """
    for boton in lista:
        if boton["cuadrado"].collidepoint(evento.pos):
            cambio_color(boton)

def detectar_jugabilidad(boton:dict,evento,elementos_juego,jugadores):
    """Descripción:

    Args:
        boton (dict): Diccionario donde sacamos los datos.
        evento (_type_): evento capturado.
        elementos_juego (_type_): _description_
        jugadores (_type_): _description_
    """
    if boton["cuadrado"].collidepoint(evento.pos):
        boton["accion"](boton["lista_parametros"],elementos_juego,jugadores)

def detectar_cambio_nombre(boton):
    """Descripción:

    Args:
        boton (_type_): _description_
    """
    if boton["activo"]: 
        boton["texto"]= "REINICIO"

def detectar_escritura(boton,evento):
    """Descripción:

    Args:
        boton (_type_): _description_
        evento (_type_): _description_
    """
    boton["accion"](boton,evento)

def crear_listas_parametros(pantalla_config,listas,colores,matriz)-> list:
    """Descripción:

    Args:
        pantalla_config (_type_): _description_
        listas (_type_): _description_
        colores (_type_): _description_
        matriz (_type_): _description_

    Returns:
        list: _description_
    """
    lista = []
    parametros_jugar = [10,matriz,listas,pantalla_config,colores]
    parametros_boton_nombre_uno = [pantalla_config,("Arial",20),colores["negro"],(795,50),None]
    parametros_boton_nombre_dos = [pantalla_config,("Arial",20),colores["negro"],(797,629),None]

    lista.append(parametros_jugar)
    lista.append(parametros_boton_nombre_uno)
    lista.append(parametros_boton_nombre_dos)

    return lista

def detectar_accion(boton_jugar,elementos_juego,jugadores,evento):
    """Descripción:

    Args:
        boton_jugar (_type_): _description_
        elementos_juego (_type_): _description_
        jugadores (_type_): _description_
        evento (_type_): _description_
    """
    if boton_jugar["cuadrado"].collidepoint(evento.pos):
        cambio_color(boton_jugar)

    detectar_jugabilidad(boton_jugar,evento,elementos_juego,jugadores)

    detectar_cambio_nombre(boton_jugar)

def verificar_botones_musicales(lista_botones, evento):
    """Descripción:

    Args:
        lista_botones (_type_): _description_
        evento (_type_): _description_
    """
    for boton in lista_botones:
        if boton["rectangulo"].collidepoint(evento.pos):
            boton["accion"]()

