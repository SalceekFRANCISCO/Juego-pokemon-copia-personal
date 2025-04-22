import pygame
from Funciones_pygame.Musica import *

def crear_lista_cuadrados(ventana, colores) -> list:
    """
    Descripción: Crea una lista de cuadrados en la ventana con colores y posiciones predeterminadas.

    Args:
        ventana (Surface): La ventana de Pygame donde se dibujarán los cuadrados.
        colores (dict): Diccionario con los colores a usar para cada cuadrado.

    Returns:
        list: Lista de diccionarios que contienen los cuadrados con sus propiedades.
    """
    lista = []
    colores = [colores['rojo'], colores['azul_claro'], colores['blanco'], colores['negro'], colores['negro']]
    posiciones = [(56, 180), (162, 180), (911, 127), (385, 80), (385, 360)]
    dimensiones = [(100, 215), (100, 215), (135, 170), (520, 260), (520, 260)]

    for i in range(len(colores)):
        cuadrado = crear_cuadrado(ventana, colores[i], posiciones[i], dimensiones[i])
        lista.append(cuadrado)

    return lista

def crear_lista_rectangulo_con_texto(ventana, colores, boton_jugar):
    """
    Descripción: Crea una lista de rectángulos con texto en la ventana.

    Args:
        ventana (Surface): La ventana de Pygame donde se dibujarán los rectángulos.
        colores (dict): Diccionario de colores.
        boton_jugar (dict): Datos del botón de jugar.

    Returns:
        list: Lista de rectángulos con texto.
    """
    lista = [boton_jugar]

    fuente = ("Arial", 20)
    posiciones = [(911, 366), (911, 445), (911, 524)]
    dimensiones = (200, 60)
    textos = ["Atributo Sorteado", "Ganador ronda", "Ganador partida"]

    for i in range(len(posiciones)):
        rectangulo = crear_cuadrado(ventana, colores["blanco"], posiciones[i], dimensiones, fuente, textos[i])
        lista.append(rectangulo)

    return lista

def crear_lista_botones_musicales(ventana) -> list:
    """
    Descripción: Crea una lista de botones musicales con sus respectivas acciones.

    Args:
        ventana (Surface): La ventana de Pygame donde se dibujarán los botones.

    Returns:
        list: Lista de botones musicales con sus propiedades.
    """
    lista = []
    posiciones = [(21, 453), (98, 453), (164, 453), (236, 453), (307, 453), (21, 531), (104, 531)]
    dimensiones = (50, 50)
    acciones = [reproducir_musica, pausar_musica, detener_musica, subir_volumen, bajar_volumen, mutear, desmutear]
    imagenes = [r"Musica\Img_musica\play.png", r"Musica\Img_musica\pause.png", r"Musica\Img_musica\stop.png", 
                r"Musica\Img_musica\up.png", r"Musica\Img_musica\down.png", r"Musica\Img_musica\mute.png", 
                r"Musica\Img_musica\unmute.png"]

    for i in range(len(posiciones)):
        cuadrado = crear_boton_musical(ventana, posiciones[i], dimensiones, acciones[i], imagenes[i])
        lista.append(cuadrado)

    return lista

def crear_diccionario_colores() -> list:
    """
    Descripción: Crea un diccionario con los colores predeterminados para el juego.

    Returns:
        dict: Diccionario con los colores definidos.
    """
    pygame.init()

    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)
    AZUL_CLARO = (0, 150, 255)
    VERDE = (0, 255, 0)
    BLANCO = (255, 255, 255)
    DORADO = (204, 153, 0)
    GRIS = (128, 128, 128)
    ROSA = (255, 192, 203)

    colores = crear_colores(NEGRO, ROJO, AZUL, AZUL_CLARO, VERDE, BLANCO, DORADO, GRIS, ROSA)

    return colores

def crear_diccionario_listas() -> dict:
    """
    Descripción: Crea un diccionario para almacenar listas vacías que se utilizarán durante el juego.

    Returns:
        dict: Diccionario con listas vacías para los jugadores, cartas y más.
    """
    listas = {}
    listas["lista_jugador_uno"] = [] 
    listas["lista_jugador_dos"] = [] 
    listas["cartas_jugadores"] = [] 
    listas["lista_cartas"] = [] 
    listas["cartas_meza"] = [] 

    return listas

def crear_banderas_pantalla_inicial(ventana, primer_pantalla, empezar_juego, bandera_principal):
    """
    Descripción: Crea un diccionario con banderas y datos de la pantalla inicial.

    Args:
        ventana (Surface): La ventana de Pygame.
        primer_pantalla (bool): Bandera que indica si es la primera pantalla.
        empezar_juego (bool): Bandera que indica si se debe empezar el juego.
        bandera_principal (bool): Bandera principal que controla el flujo del juego.

    Returns:
        dict: Diccionario con las banderas de la pantalla inicial.
    """
    pre_pantalla = {}
    pre_pantalla["ventana"] = ventana
    pre_pantalla["primer_pantalla"] = primer_pantalla
    pre_pantalla["empezar_juego"] = empezar_juego
    pre_pantalla["bandera_principal"] = bandera_principal

    return pre_pantalla

def crear_datos_pantalla(ventana, fondo, fondo_2, colores) -> dict:
    """
     Descripción: Crea y retorna los datos de la pantalla, como colores, imágenes y elementos gráficos.

    Args:
        ventana (Surface): La ventana de Pygame.
        fondo (Surface): Imagen de fondo principal.
        fondo_2 (Surface): Imagen de fondo secundario.
        colores (dict): Diccionario de colores.

    Returns:
        dict: Diccionario con los elementos gráficos para la pantalla.
    """
    lista_cuadrados = crear_lista_cuadrados(ventana, colores)

    pokebola = crear_diccionario_imagen(ventana, "Poke_fotos\pokebola.png", (370, 145), (530, 425))
    carta_1 = crear_cuadrado(ventana, colores["azul_claro"], (450, 26), (340, 245))
    carta_2 = crear_cuadrado(ventana, colores["rojo"], (450, 415), (340, 245))

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

def crear_datos_juego(ventana, colores, boton_jugar, lista_botones_musicales) -> dict:
    """
    Descripción: Crea un diccionario con los elementos del juego, como botones y música.

    Args:
        ventana (Surface): La ventana de Pygame.
        colores (dict): Diccionario de colores.
        boton_jugar (dict): El botón de jugar.
        lista_botones_musicales (list): Lista de botones para controlar la música.

    Returns:
        dict: Diccionario con los datos del juego.
    """
    lista_rect_texto = crear_lista_rectangulo_con_texto(ventana, colores, boton_jugar)

    juego = {}
    juego["lista_rect_texto"] = lista_rect_texto
    juego["lista_botones_musicales"] = lista_botones_musicales

    return juego

def crear_cuadrado(ventana, color: tuple, posicion: tuple, dimensiones: tuple, fuente=None, texto=None):
    """
    Descripción: Crea un cuadrado o rectángulo en la ventana con color, posición y dimensiones.

    Args:
        ventana (Surface): La ventana de Pygame.
        color (tuple): El color del cuadrado.
        posicion (tuple): La posición (x, y) del cuadrado.
        dimensiones (tuple): Las dimensiones (ancho, alto) del cuadrado.
        fuente (tuple, opcional): La fuente para el texto (si se proporciona).
        texto (str, opcional): El texto que se mostrará en el cuadrado (si se proporciona).

    Returns:
        dict: Diccionario con las propiedades del cuadrado.
    """
    cuadrado = {}
    cuadrado["ventana"] = ventana
    cuadrado["color_actual"] = color
    cuadrado["cuadrado"] = pygame.Rect(posicion[0], posicion[1], dimensiones[0], dimensiones[1])

    if fuente is not None:
        cuadrado["fuente"] = crear_fuente(fuente[0], fuente[1])

    if texto is not None:
        cuadrado["texto"] = texto

    return cuadrado

def crear_colores(NEGRO, ROJO, AZUL, AZUL_CLARO, VERDE, BLANCO, DORADO, GRIS, ROSA) -> dict:
    """
    Descripción: Crea un diccionario de colores definidos para usar en el juego.

    Args:
        NEGRO (tuple): Color negro en formato RGB.
        ROJO (tuple): Color rojo en formato RGB.
        AZUL (tuple): Color azul en formato RGB.
        AZUL_CLARO (tuple): Color azul claro en formato RGB.
        VERDE (tuple): Color verde en formato RGB.
        BLANCO (tuple): Color blanco en formato RGB.
        DORADO (tuple): Color dorado en formato RGB.
        GRIS (tuple): Color gris en formato RGB.
        ROSA (tuple): Color rosa en formato RGB.

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

def crear_boton(ventana, fuente, colores: tuple, posicion: tuple, dimensiones: tuple, accion, lista_parametros=None, texto=None) -> dict:
    """
    Descripción: Crea un botón con su respectiva fuente, colores y acción.

    Args:
        ventana (Surface): La ventana de Pygame.
        fuente (tuple): Tupla con el tipo de fuente y tamaño.
        colores (tuple): Tupla con los colores para el botón.
        posicion (tuple): La posición (x, y) del botón.
        dimensiones (tuple): Las dimensiones (ancho, alto) del botón.
        accion (func): Función que se ejecutará al presionar el botón.
        lista_parametros (list, opcional): Lista de parámetros para la acción del botón.
        texto (str, opcional): Texto que se mostrará en el botón.

    Returns:
        dict: Diccionario con las propiedades del botón.
    """
    boton = {}
    boton["ventana"] = ventana
    boton["fuente"] = crear_fuente(fuente[0], fuente[1])
    boton["color_activo"] = colores["dorado"]
    boton["color_inactivo"] = colores["blanco"]
    boton["activo"] = False
    boton["cuadrado"] = pygame.Rect(posicion[0], posicion[1], dimensiones[0], dimensiones[1])
    boton["color_actual"] = colores["blanco"]
    boton["accion"] = accion

    if lista_parametros is not None:
        boton["lista_parametros"] = lista_parametros

    if texto is not None:
        boton["texto"] = texto

    return boton

def crear_boton_musical(ventana, posicion: tuple, dimensiones: tuple, accion, imagen) -> dict:
    """
    Descripción: Crea un botón musical con una imagen y acción.

    Args:
        ventana (Surface): La ventana de Pygame.
        posicion (tuple): La posición (x, y) del botón.
        dimensiones (tuple): Las dimensiones (ancho, alto) del botón.
        accion (func): Acción que se ejecutará al presionar el botón.
        imagen (str): Ruta de la imagen del botón.

    Returns:
        dict: Diccionario con las propiedades del botón musical.
    """
    boton_musical = {}
    boton_musical["ventana"] = ventana
    boton_musical["dimensiones"] = dimensiones
    boton_musical["posicion"] = posicion
    boton_musical["accion"] = accion
    boton_musical["activo"] = False

    boton_musical["contenido"] = cargar_imagenes(imagen, boton_musical["dimensiones"])

    boton_musical["rectangulo"] = boton_musical["contenido"].get_rect()
    boton_musical["rectangulo"].topleft = boton_musical["posicion"]

    return boton_musical

def crear_diccionario_imagen(ventana, path, coordenadas, dimensiones) -> dict:
    """
    Descripción: Crea un diccionario con la información de una imagen.

    Args:
        ventana (Surface): La ventana de Pygame.
        path (str): Ruta de la imagen.
        coordenadas (tuple): Coordenadas de la imagen en la ventana.
        dimensiones (tuple): Dimensiones (ancho, alto) para la imagen.

    Returns:
        dict: Diccionario con los datos de la imagen.
    """
    imagen = {}
    imagen_cargada = cargar_imagenes(path, dimensiones)
    imagen["imagen_final"] = imagen_cargada
    imagen["ventana"] = ventana
    imagen["coordenadas"] = coordenadas

    return imagen

def generar_texto_renderizado(pantalla, fuente: tuple, texto_escrito: str, color_texto: tuple, posicion: tuple, color_fondo_texto: tuple) -> dict:
    """
    Descripción: Genera el texto renderizado listo para ser mostrado en la ventana.

    Args:
        pantalla (dict): Diccionario que contiene la ventana del juego.
        fuente (tuple): Tupla con el nombre de la fuente y su tamaño.
        texto_escrito (str): El mensaje de texto que se va a mostrar.
        color_texto (tuple): Color del texto en formato RGB.
        posicion (tuple): Coordenadas (x, y) donde se mostrará el texto en la ventana.
        color_fondo_texto (tuple): Color de fondo del texto, si es necesario.

    Returns:
        dict: Diccionario con las propiedades del texto renderizado.
    """
    texto = {}
    texto["ventana"] = pantalla["ventana"]
    texto["texto_escrito"] = renderizar_mensaje((fuente[0], fuente[1]), texto_escrito, color_texto, color_fondo_texto)
    texto["posicion"] = posicion

    return texto

def renderizar_mensaje(fuente: tuple, mensaje: str, color_texto: tuple, color_fondo_texto: tuple):
    """
     Descripción: Renderiza un mensaje con la fuente, el color del texto y el color del fondo.

    Args:
        fuente (tuple): Tupla que contiene el tipo de fuente y su tamaño.
        mensaje (str): El texto que se va a renderizar.
        color_texto (tuple): Color del texto en formato RGB.
        color_fondo_texto (tuple): Color de fondo del texto (si se proporciona).

    Returns:
        Surface: Superficie con el texto renderizado.
    """
    fuente_creada = crear_fuente(fuente[0], fuente[1])
    texto_definitivo = renderizar_texto(fuente_creada, mensaje, color_texto, color_fondo_texto)

    return texto_definitivo

def crear_fuente(tipo_fuente: str, tamaño: int):
    """
    Descripción: Crea un objeto de fuente con el tipo y tamaño especificado.

    Args:
        tipo_fuente (str): El nombre de la fuente a utilizar.
        tamaño (int): El tamaño de la fuente.

    Returns:
        Font: Un objeto de fuente que puede ser utilizado para renderizar texto.
    """
    fuente = pygame.font.SysFont(tipo_fuente, tamaño)
    return fuente

def renderizar_texto(fuente_creada, mensaje: str, color_texto: tuple, color_fondo_texto: tuple = None):
    """
    Descripción: Renderiza un texto con una fuente, color de texto y color de fondo.

    Args:
        fuente_creada (Font): Objeto de fuente creado anteriormente.
        mensaje (str): El texto que se va a renderizar.
        color_texto (tuple): Color del texto en formato RGB.
        color_fondo_texto (tuple, opcional): Color del fondo del texto, si se proporciona.

    Returns:
        Surface: Superficie con el texto renderizado que se puede dibujar en la ventana.
    """
    if color_fondo_texto is not None:
        texto = fuente_creada.render(mensaje, False, color_texto, color_fondo_texto)
    else:
        texto = fuente_creada.render(mensaje, False, color_texto)

    return texto

def cargar_imagenes(path: str, coordenadas: tuple):
    """
    Descripción: Carga una imagen desde un archivo y la redimensiona a las dimensiones especificadas.

    Args:
        path (str): Ruta del archivo de la imagen.
        coordenadas (tuple): Nuevas dimensiones (ancho, alto) a las que se redimensionará la imagen.

    Returns:
        Surface: Imagen redimensionada lista para usar en la ventana.
    """
    imagen_cargada = cargar_imagen(path)
    imagen_Escalada = escalar_imagen(imagen_cargada, coordenadas)

    return imagen_Escalada

def cargar_imagen(path: str):
    """
    Descripción: Carga una imagen.

    Args:
        path (str): Ruta del archivo de la imagen.

    Returns:
        Surface: Objeto imagen cargada en formato Surface de Pygame.
    """
    imagen_cargada = pygame.image.load(path)
    return imagen_cargada

def escalar_imagen(imagen, coordenadas: tuple):
    """
    Descripción: Escala una imagen a las dimensiones especificadas.

    Args:
        imagen (Surface): La imagen que se va a redimensionar.
        coordenadas (tuple): Nuevas dimensiones (ancho, alto) a las que se escalará la imagen.

    Returns:
        Surface: Imagen escalada a las nuevas dimensiones.
    """
    imagen_Escalada = pygame.transform.scale(imagen, coordenadas)
    return imagen_Escalada
