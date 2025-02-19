import pygame
from Funciones_pygame.Visuales import *

#region
def creacion_diccionarios()->list:

    pygame.init()

    ventana = inicializar_ventana()

    NEGRO = (0,0,0)
    ROJO = (255,0,0)
    AZUL = (0,0,255)
    AZUL_CLARO = (0,150,255)
    VERDE = (0,255,0)
    BLANCO = (255,255,255)
    DORADO = (204, 153, 0)
    GRIS = (128, 128, 128)
    AMARILLO_CLARO = (254,255,145)

    cuadrado_rojo = crear_cuadrado(ventana,ROJO,(56,180),(100,215))
    cuadrado_azul = crear_cuadrado(ventana,AZUL_CLARO,(162,180),(100,215))
    cuadrado_blanco = crear_cuadrado(ventana,BLANCO,(1122,201),(135,170))
    cuadrado_negro_arriba = crear_cuadrado(ventana,NEGRO,(385,80),(520,260))
    cuadrado_negro_abajo = crear_cuadrado(ventana,NEGRO,(385,360),(520,260))

    lista_cuadrados = [cuadrado_rojo,cuadrado_azul,cuadrado_blanco,cuadrado_negro_arriba,cuadrado_negro_abajo]

    colores = crear_colores(NEGRO,ROJO,AZUL,AZUL_CLARO,VERDE,BLANCO,DORADO,GRIS)

    return [lista_cuadrados,colores]

def crear_diccionario_listas()-> dict:
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

def crear_cuadrado(ventana, color, posicion: tuple, dimensiones: tuple) -> dict:
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

def crear_datos_pantalla(ventana,colores,lista_cuadrados,jugadores):

    pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))
    carta_1 = crear_cuadrado(ventana,colores["azul_claro"],(450,26),(340,245))
    carta_2 = crear_cuadrado(ventana,colores["rojo"],(450,415),(340,245))

    pantalla_dos = {}
    pantalla_dos["ventana"] = ventana
    pantalla_dos["color_ventana"] = colores["gris"]
    pantalla_dos["lista_cuadrados"] = lista_cuadrados
    pantalla_dos["jugador_1"] = jugadores[0]
    pantalla_dos["jugador_2"] = jugadores[1]
    pantalla_dos["pokebola"] = pokebola
    pantalla_dos["carta_1"] = carta_1
    pantalla_dos["carta_2"] = carta_2
    pantalla_dos["path_json"] = "Resultados.json"
    pantalla_dos["path_csv"] = "Archivos\Pokemon_Cards_Pygame.csv"

    return pantalla_dos

def crear_datos_juego(ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos,boton_jugar):
    juego = {}
    juego["ganador_partida"] = ganador_partida_final
    juego["atributo"] = atributo
    juego["boton_nombre_uno"] = boton_nombre_uno
    juego["boton_nombre_dos"] = boton_nombre_dos
    juego["boton_jugar"] = boton_jugar

    return juego

# def generar_estado_accion (bandera:bool,texto_pantalla):
#     accion = {}
#     accion["bandera"] = bandera
#     accion["texto_pantalla"] = texto_pantalla

#     return accion

############################# INTERACCION #######################################################################################
def cambio_color(boton):
    """
    Cambia el color de un campo de entrada basado en su estado (activo/inactivo).

    Args:
        boton (dict): Diccionario del campo de entrada.
    """
    boton["activo"] = not boton["activo"]
    if boton["activo"]:
        boton["color_actual"] = boton["color_activo"] 
    else:
        boton["color_actual"] = boton["color_inactivo"]

def generar_texto_renderizado (pantalla,fuente:tuple,texto_escrito,color_texto:tuple,posicion:tuple,color_fondo_texto)->dict:
    """la función genera texto listo para renderizar.

    Args:
        pantalla (_type_): _description_
        fuente (_type_): _description_
        texto_escrito (_type_): _description_
        color_texto (_type_): _description_
        posicion (_type_): _description_
        color_fondo_texto (_type_): _description_

    Returns:
        dict: diccionario con los datos del texto
    """
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

    # print(f"Texto actual del botón: {boton['texto']}")
    return boton["texto"]

def crear_boton(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,accion,lista_parametros,texto=None) -> dict:
    boton = {}
    boton["ventana"] = ventana
    boton["fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
    boton["color_activo"] = colores["dorado"]
    boton["color_inactivo"] = colores["blanco"]
    boton["activo"] = False
    boton["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
    boton["color_actual"] = colores["blanco"]
    boton["accion"] = accion
    boton["lista_parametros"] = lista_parametros

    if texto != None:
        boton["texto"] = texto

    return boton

def detectar_cambio_color(lista,evento):
    for boton in lista:
        if boton["cuadrado"].collidepoint(evento.pos):
            cambio_color(boton)

def detectar_jugabilidad(boton,evento,elementos_juego):
    if boton["cuadrado"].collidepoint(evento.pos):
        tiempo_inicial = pygame.time.get_ticks()  
        cronometro_activo = True 
        boton["accion"](boton["lista_parametros"],elementos_juego)
        detectar_cambio_nombre(boton)

def detectar_cambio_nombre(boton):
    if boton["activo"]: 
        boton["texto"]= "REINICIO"
#endregion

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

def generar_estado_accion(bandera:bool,texto_pantalla):
    accion = {}
    accion["bandera"] = bandera
    accion["texto_pantalla"] = texto_pantalla

    return accion

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

#region

# def crear_diccionario_pantalla(ventana, GRIS, lista_cuadrados, boton_jugar, reemplazo_boton, 
#                                pokebola, carta_1, carta_2, jugadores, 
#                                path_json, path_csv, boton_ganador_partida,atributo,boton_nombre_uno,boton_nombre_dos) -> dict:
#     """
#     Crea un diccionario que almacena los datos principales de la pantalla.

#     Args:
#         ventana: Superficie de Pygame donde se dibujarán los elementos.
#         GRIS: Color de fondo de la ventana.
#         lista_cuadrados (list): Lista de cuadrados en la pantalla.
#         boton_jugar: Botón de inicio del juego.
#         reemplazo_boton: Botón de reemplazo para alguna acción específica.
#         boton_reinicio: Botón para reiniciar el juego.
#         pokebola: Imagen o referencia a la pokebola.
#         carta_1, carta_2: Cartas asociadas a los jugadores.
#         jugadores (list): Lista de jugadores (jugador 1 y jugador 2).
#         path_json (str): Ruta al archivo JSON relacionado.
#         path_csv (str): Ruta al archivo CSV relacionado.

#     Returns:
#         dict: Diccionario con los datos de la pantalla.
#     """
#     pantalla = {}
#     pantalla["ventana"] = ventana
#     pantalla["color_ventana"] = GRIS
#     pantalla["lista_cuadrados"] = lista_cuadrados
#     pantalla["boton_jugar"] = boton_jugar
#     pantalla["reemplazo_nombre"] = reemplazo_boton
#     # pantalla["boton_reinicio"] = boton_reinicio
#     pantalla["pokebola"] = pokebola
#     pantalla["carta_1"] = carta_1
#     pantalla["carta_2"] = carta_2
#     pantalla["jugador_1"] = jugadores[0]
#     pantalla["jugador_2"] = jugadores[1]
#     pantalla["path_json"] = path_json
#     pantalla["path_csv"] = path_csv
#     pantalla["ganador_partida"] = boton_ganador_partida
#     pantalla["atributo"] = atributo
#     pantalla["boton_nombre_uno"] = boton_nombre_uno
#     pantalla["boton_nombre_dos"] = boton_nombre_dos

#     return pantalla


# def procesar_entrada_texto (pantalla:dict,fuente:tuple,color_texto:tuple,boton_nombre:dict,posicion_texto: tuple,evento,color_fondo_texto):#!usa la ventana
# def procesar_entrada_texto (parametros):
#     pantalla = parametros[0]
#     fuente = parametros[1]
#     color_texto = parametros[2]
#     boton_nombre = parametros[3]
#     posicion_texto =  parametros[4]
#     evento =  parametros[5]
#     color_fondo_texto = parametros[6]


#     texto_pantalla = ""
#     nombre_final = escribir_teclado(boton_nombre,evento)

#     texto_pantalla = generar_texto_renderizado (pantalla,fuente,nombre_final,color_texto,posicion_texto,color_fondo_texto)
            
#     return texto_pantalla

#endregion