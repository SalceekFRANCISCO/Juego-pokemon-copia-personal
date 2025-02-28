import pygame
from Funciones_pygame.Musica import *

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
    cartas_meza = crear_cuadrado(ventana,BLANCO,(911,127),(135,170))
    cuadrado_negro_arriba = crear_cuadrado(ventana,NEGRO,(385,80),(520,260))
    cuadrado_negro_abajo = crear_cuadrado(ventana,NEGRO,(385,360),(520,260))

    lista_cuadrados = [cuadrado_rojo,cuadrado_azul,cartas_meza,cuadrado_negro_arriba,cuadrado_negro_abajo]

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

def crear_pantalla_datos(ventana,colores,primer_pantalla,empezar_juego,bandera_principal):
    pre_pantalla = {}
    pre_pantalla["ventana"] = ventana
    pre_pantalla["color_ventana"] = colores["azul"]
    pre_pantalla["primer_pantalla"] = primer_pantalla
    pre_pantalla["empezar_juego"] = empezar_juego
    pre_pantalla["bandera_principal"] = bandera_principal

    return pre_pantalla

def crear_datos_pantalla(ventana) -> dict:

    diccionarios = creacion_diccionarios()
    lista_cuadrados = diccionarios[0]
    colores = diccionarios[1]

    pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))
    carta_1 = crear_cuadrado(ventana,colores["azul_claro"],(450,26),(340,245))
    carta_2 = crear_cuadrado(ventana,colores["rojo"],(450,415),(340,245))

    pantalla = {}
    pantalla["ventana"] = ventana
    pantalla["color_ventana"] = colores["gris"]
    pantalla["lista_cuadrados"] = lista_cuadrados
    pantalla["pokebola"] = pokebola
    pantalla["carta_1"] = carta_1
    pantalla["carta_2"] = carta_2
    pantalla["path_json"] = "Resultados.json"
    pantalla["path_csv"] = "Archivos\Pokemon_Cards_Pygame.csv"

    return pantalla

def crear_texto_cuadrado(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,texto=None) -> dict:
    """
    Crea un diccionario que representa un campo de entrada (input) en Pygame.

    Args:
        ventana: Superficie de Pygame donde se dibujará el campo de entrada.
        fuente (tuple): Tipo y tamaño de fuente a utilizar (nombre, tamaño).
        colores (dict): Diccionario con los colores disponibles.
        posicion (tuple): Coordenadas (x, y) del campo de entrada.
        dimensiones (tuple): Ancho y alto del campo de entrada.
        texto (str): Texto inicial del campo de entrada.

    Returns:
        dict: Diccionario con los datos del campo de entrada.
    """
    input = {}
    input["ventana"] = ventana
    input["fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
    input["color_actual"] = colores["blanco"]
    input["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])

    if texto != None:
        input["texto"] = texto 

    return input

def crear_datos_juego(colores,boton_jugar,lista_botones_musicales) -> dict:
    ventana = inicializar_ventana()

    atributo = crear_texto_cuadrado(ventana,("Arial",20),colores,(911,366),(200,60),"Atributo Sorteado")
    ganador_ronda = crear_texto_cuadrado(ventana,("Arial",20),colores,(911,445),(200,60),"Ganador ronda")
    ganador_partida_final = crear_texto_cuadrado(ventana,("Arial",20),colores,(911,524),(200,60),"Ganador partida")

    lista_rect_texto = [atributo,ganador_ronda,ganador_partida_final,boton_jugar]

    juego = {}
    juego["boton_jugar"] = boton_jugar
    juego["lista_rect_texto"] = lista_rect_texto
    juego["lista_botones_musicales"] = lista_botones_musicales

    return juego

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

def crear_boton_musical(ventana, posicion:tuple, dimensiones:tuple,accion,imagen=None) -> dict:
    boton_musical = {}
    boton_musical["ventana"] = ventana
    boton_musical["dimensiones"] = dimensiones
    boton_musical["posicion"] = posicion
    boton_musical["accion"] = accion
    boton_musical["activo"] = False

    if boton_musical != None:
        img = pygame.image.load(imagen)
        boton_musical["contenido"] = pygame.transform.scale(img,boton_musical["dimensiones"])

    boton_musical["rectangulo"] = boton_musical["contenido"].get_rect()
    boton_musical["rectangulo"].topleft = boton_musical["posicion"]


    return boton_musical

def crear_botones(ventana):          
    boton_play = crear_boton_musical(ventana,(21,453),(50,50),reproducir_musica,r"Musica\Img_musica\play.png")
    boton_pause = crear_boton_musical(ventana,(98,453),(50,50),pausar_musica,r"Musica\Img_musica\pause.png")
    boton_stop = crear_boton_musical(ventana,(164,453),(50,50),detener_musica,r"Musica\Img_musica\stop.png")
    boton_up = crear_boton_musical(ventana,(236,453),(50,50),subir_volumen,r"Musica\Img_musica\up.png")
    boton_down = crear_boton_musical(ventana,(307,453),(50,50),bajar_volumen,r"Musica\Img_musica\down.png")
    boton_mute = crear_boton_musical(ventana,(21,531),(50,50),mutear,r"Musica\Img_musica\mute.png")
    boton_unmute = crear_boton_musical(ventana,(104,531),(50,50),desmutear,r"Musica\Img_musica\unmute.png")

    lista = [boton_play, boton_pause, boton_stop, boton_up, boton_down, boton_mute, boton_unmute]
    
    return lista

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

def crear_temporizador(ventana, fuente, posicion, dimensiones, tiempo, color) -> dict:
    """
    Crea un temporizador para mostrar en pantalla.

    Args:
        ventana (Surface): Superficie donde se dibuja.
        fuente (tuple): Tipo y tamaño de la fuente.
        posicion (tuple): Coordenadas del temporizador.
        dimensiones (tuple): Dimensiones del rectángulo del temporizador.
        tiempo (str): Tiempo inicial a mostrar.
        color (tuple): Color del texto.

    Returns:
        dict: Diccionario con datos del temporizador.
    """
    texto_superficie = renderizar_mensaje((fuente[0],fuente[1]),tiempo,color,None)

    temporizador = {}
    temporizador["ventana"] = ventana
    temporizador["rectangulo"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
    temporizador["texto"] = texto_superficie

    return temporizador

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

def cargar_imagenes(path: str, coordenadas:tuple):
    """
    Carga y escala una imagen.

    Args:
        path (str): Ruta de la imagen.
        coordenadas (tuple): Dimensiones para escalar la imagen.

    Returns:
        Surface: Imagen escalada.
    """
    imagen_cargada = cargar_imagen(path)
    imagen_Escalada = escalar_imagen(imagen_cargada,coordenadas)

    return imagen_Escalada

def cargar_imagen(path:str):
    """
    Carga una imagen desde un archivo.

    Args:
        path (str): Ruta de la imagen.

    Returns:
        Surface: Imagen cargada.
    """
    imagen_cargada = pygame.image.load(path)

    return imagen_cargada

def escalar_imagen(imagen, coordenadas:tuple):
    """
    Escala una imagen a las dimensiones especificadas.

    Args:
        imagen (Surface): Imagen a escalar.
        coordenadas (tuple): Nuevas dimensiones (ancho, alto).

    Returns:
        Surface: Imagen escalada.
    """
    imagen_Escalada = pygame.transform.scale(imagen, coordenadas)

    return imagen_Escalada
