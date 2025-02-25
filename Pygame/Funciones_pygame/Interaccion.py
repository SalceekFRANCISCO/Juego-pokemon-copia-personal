import pygame
from Funciones_pygame.Diccionarios import *

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

def crear_matriz_jerarquias()-> list[list]:

    matriz_jerarquias_mezclada = [["Agua", ("Fuego", "Tierra")],
                    [("Electricidad", "Fuego"),"Tierra"],
                    ["Aire",("Tierra","Agua")],
                    [("Aire", "Hielo"),"Fuego"],
                    ["Electricidad",("Agua", "Hielo")], 
                    [("Normal", "Fuego"),"Psíquico"],
                    ["Normal",("Agua", "Aire")],
                    [("Tierra", "Aire"),"Hielo"]]

    return matriz_jerarquias_mezclada

def escribir_teclado(boton, evento)->str:
    if boton["activo"]:
        if evento.key == pygame.K_BACKSPACE:
            boton["texto"] = boton["texto"][:-1]

        elif evento.key == pygame.K_RCTRL:
            boton["texto"] = ""

        elif evento.key == pygame.K_RETURN:
            boton["activo"] = False
            boton["color_actual"] = boton["color_inactivo"]
        else:
            boton["texto"] += evento.unicode

    return boton["texto"]

def cambio_color(boton:dict):
    """
    Cambia el color de un campo de entrada basado en su estado (activo/inactivo).

    Args:
        boton (dict): Diccionario del campo de entrada.
    """
    boton["activo"] = not boton["activo"]
    print(boton["texto"])

    if boton["texto"] != "JUGAR" and boton["texto"] != "":
        boton["color_actual"] = boton["color_inactivo"]

    if boton["activo"]:
        boton["color_actual"] = boton["color_activo"] 
    else:
        boton["color_actual"] = boton["color_inactivo"]

def detectar_cambio_color(lista,evento):
    for boton in lista:
        if boton["cuadrado"].collidepoint(evento.pos):
            cambio_color(boton)

def detectar_jugabilidad(boton,evento,elementos_juego):
    if boton["cuadrado"].collidepoint(evento.pos):
        tiempo_inicial = pygame.time.get_ticks()  
        cronometro_activo = True 
        boton["accion"](boton["lista_parametros"],elementos_juego)

def detectar_cambio_nombre(boton):
    if boton["activo"]: 
        boton["texto"]= "REINICIO"
        print(boton["texto"])

def detectar_escritura(boton,evento):
    texto_pantalla = boton["accion"](boton["lista_parametros"],boton,evento)
    bandera = True
    accion = generar_estado_accion(bandera,texto_pantalla)

    return accion

def procesar_entrada_texto(parametros:list,boton_nombre:dict,evento)->dict:
    """Registra el texto que se ingresa por teclado

    Args:
        parametros (list): lista de parametros que se utilizaran
        boton_nombre (dict): diccionario de donde sacaremos los datos
        evento (_type_): ele tipo de evento que se registro

    Returns:
        dict: retorna un diccionario con los datos del texto
    """
    pantalla = parametros[0]
    fuente = parametros[1]
    color_texto = parametros[2]
    posicion_texto =  parametros[3]
    color_fondo_texto = parametros[4]

    nombre_final = escribir_teclado(boton_nombre,evento)

    texto_pantalla = generar_texto_renderizado(pantalla,fuente,nombre_final,color_texto,posicion_texto,color_fondo_texto)
            
    return texto_pantalla

def agrupar_acciones(accion_a,accion_b):
    lista = []
    lista.append(accion_a)
    lista.append(accion_b)

    return lista

def crear_listas_parametros(pantalla_config,listas,colores,matriz,cronometro,tiempo)-> list:
    lista = []
    parametros_jugar = [5,matriz,listas,pantalla_config,colores,cronometro,tiempo]
    parametros_boton_nombre_uno = [pantalla_config,("Arial",20),colores["negro"],(795,50),None]
    parametros_boton_nombre_dos = [pantalla_config,("Arial",20),colores["negro"],(797,629),None]

    lista.append(parametros_jugar)
    lista.append(parametros_boton_nombre_uno)
    lista.append(parametros_boton_nombre_dos)

    return lista

def jugabilidad(lista_botones,elementos_juego,evento):
    detectar_cambio_color(lista_botones,evento)

    detectar_jugabilidad(lista_botones[2],evento,elementos_juego)

    detectar_cambio_nombre(lista_botones[2])

def veriificar_accion_botones(lista_botones, evento):
    for boton in lista_botones:
        if boton["rectangulo"].collidepoint(evento.pos):
            boton["accion"]()
