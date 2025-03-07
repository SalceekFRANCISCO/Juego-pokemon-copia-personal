import pygame
from Funciones_pygame.Musica import *

#  los conjuntos (set) solo pueden contener elementos inmutables (hashables), como números, cadenas y tuplas

def crear_lista_cuadrados(ventana,colores)->list:
    lista = []
    colores = [colores['rojo'], colores['azul_claro'], colores['blanco'], colores['negro'], colores['negro']]
    posiciones = [(56, 180), (162, 180), (911, 127), (385, 80), (385, 360)]
    dimensiones = [(100, 215), (100, 215), (135, 170), (520, 260), (520, 260)]

    for i in range(len(colores)):
        cuadrado = crear_cuadrado(ventana,colores[i],posiciones[i],dimensiones[i])
        lista.append(cuadrado)
    
    return lista

def crear_lista_rectangulo_con_texto(ventana,colores,boton_jugar):
    lista = [boton_jugar]

    fuente = ("Arial",20)
    posiciones = [(911, 366), (911, 445), (911, 524)]
    dimensiones = (200, 60)
    textos = ["Atributo Sorteado","Ganador ronda","Ganador partida"]

    for i in range(len(posiciones)):
        rectangulo = crear_cuadrado(ventana,colores["blanco"],posiciones[i],dimensiones,fuente,textos[i]) 
        lista.append(rectangulo)
    
    return lista

def crear_lista_botones_musicales(ventana)->list:
    lista = []
    posiciones = [(21,453),(98,453),(164,453),(236,453),(307,453),(21,531),(104,531)]
    dimensiones = (50, 50)
    acciones = [reproducir_musica,pausar_musica,detener_musica,subir_volumen,bajar_volumen,mutear,desmutear]
    imagenes = [r"Musica\Img_musica\play.png",r"Musica\Img_musica\pause.png",r"Musica\Img_musica\stop.png",r"Musica\Img_musica\up.png",r"Musica\Img_musica\down.png",r"Musica\Img_musica\mute.png",r"Musica\Img_musica\unmute.png"]

    for i in range(len(posiciones)):
        cuadrado = crear_boton_musical(ventana,posiciones[i],dimensiones,acciones[i],imagenes[i])
        lista.append(cuadrado)
    
    return lista

def crear_diccionario_colores()->list:
    pygame.init()

    NEGRO = (0,0,0)
    ROJO = (255,0,0)
    AZUL = (0,0,255)
    AZUL_CLARO = (0,150,255)
    VERDE = (0,255,0)
    BLANCO = (255,255,255)
    DORADO = (204, 153, 0)
    GRIS = (128, 128, 128)
    ROSA = (255, 192, 203)

    colores = crear_colores(NEGRO,ROJO,AZUL,AZUL_CLARO,VERDE,BLANCO,DORADO,GRIS,ROSA)

    return colores

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

def crear_banderas_pantalla_inicial(ventana,primer_pantalla,empezar_juego,bandera_principal):
    pre_pantalla = {}
    pre_pantalla["ventana"] = ventana
    pre_pantalla["primer_pantalla"] = primer_pantalla
    pre_pantalla["empezar_juego"] = empezar_juego
    pre_pantalla["bandera_principal"] = bandera_principal

    return pre_pantalla

def crear_datos_pantalla(ventana,fondo,fondo_2,colores) -> dict:

    lista_cuadrados = crear_lista_cuadrados(ventana,colores)

    pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))
    carta_1 = crear_cuadrado(ventana,colores["azul_claro"],(450,26),(340,245))
    carta_2 = crear_cuadrado(ventana,colores["rojo"],(450,415),(340,245))

    pantalla = {}
    pantalla["ventana"] = ventana
    pantalla["fondo"] = fondo
    pantalla["fondo_2"] = fondo_2
    pantalla["color_ventana"] = colores["gris"]
    pantalla["lista_cuadrados"] = lista_cuadrados
    pantalla["pokebola"] = pokebola
    pantalla["carta_1"] = carta_1
    pantalla["carta_2"] = carta_2
    pantalla["path_json"] = "Resultados.json"
    pantalla["path_csv"] = "Archivos\Pokemon_Cards_Pygame.csv"

    return pantalla

def crear_datos_juego(ventana,colores,boton_jugar,lista_botones_musicales) -> dict:

    lista_rect_texto = crear_lista_rectangulo_con_texto(ventana,colores,boton_jugar)

    juego = {}
    juego["lista_rect_texto"] = lista_rect_texto
    juego["lista_botones_musicales"] = lista_botones_musicales

    return juego

def crear_cuadrado(ventana,color:tuple,posicion:tuple,dimensiones:tuple,fuente=None,texto=None):
    cuadrado = {}
    cuadrado["ventana"]= ventana
    cuadrado["color_actual"]= color
    cuadrado["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])

    if fuente != None:
        cuadrado["fuente"] = crear_fuente(fuente[0],fuente[1])
    
    if texto != None:
        cuadrado["texto"] = texto 

    return cuadrado

def crear_colores(NEGRO, ROJO, AZUL, AZUL_CLARO, VERDE, BLANCO, DORADO, GRIS, ROSA) -> dict:
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
    colores["rosa"] = ROSA

    return colores

def crear_boton(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,accion,lista_parametros=None,texto=None) -> dict:
    boton = {}
    boton["ventana"] = ventana
    boton["fuente"] = crear_fuente(fuente[0],fuente[1])
    boton["color_activo"] = colores["dorado"]
    boton["color_inactivo"] = colores["blanco"]
    boton["activo"] = False
    boton["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
    boton["color_actual"] = colores["blanco"]
    boton["accion"] = accion

    if lista_parametros != None:
        boton["lista_parametros"] = lista_parametros

    if texto != None:
        boton["texto"] = texto

    return boton

def crear_boton_musical(ventana, posicion:tuple, dimensiones:tuple,accion,imagen) -> dict:
    boton_musical = {}
    boton_musical["ventana"] = ventana
    boton_musical["dimensiones"] = dimensiones
    boton_musical["posicion"] = posicion
    boton_musical["accion"] = accion
    boton_musical["activo"] = False

    boton_musical["contenido"]= cargar_imagenes(imagen,boton_musical["dimensiones"])

    boton_musical["rectangulo"] = boton_musical["contenido"].get_rect()
    boton_musical["rectangulo"].topleft = boton_musical["posicion"]


    return boton_musical

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