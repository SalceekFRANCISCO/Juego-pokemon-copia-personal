import pygame
from Funciones_pygame.Dibujar import *
from Funciones_pygame.Interaccion import *

def setear_pantalla(pantalla_config, elementos_juego, jugadores, colores):
    """
    Descripción: Configura y dibuja todos los elementos en la pantalla inicial del juego, como los fondos, botones, texto, imágenes, etc.

    Args:
        pantalla_config (dict): Configuración de la pantalla, como la superficie, colores, etc.
        elementos_juego (dict): Elementos específicos del juego como botones, cuadros y otros objetos gráficos.
        jugadores (list): Lista con los nombres de los jugadores para mostrarlos en pantalla.
        colores (dict): Diccionario con los colores que se usarán para el texto, los botones y otros elementos gráficos.
    """
    dibujar_fondo(pantalla_config)

    dibujar(elementos_juego["lista_botones_musicales"],dibujar_botones_musicales)

    dibujar(pantalla_config["lista_cuadrados"],dibujar_lista_cuadrados)

    mostrar_texto(pantalla_config,("Arial",30),jugadores[0],colores["negro"],(795,40),colores["rosa"])
    mostrar_texto(pantalla_config,("Arial",30),jugadores[1],colores["negro"],(797,623),colores["rosa"])

    dibujar_textos_en_cuadrados(elementos_juego["lista_rect_texto"],colores)

    dibujar_imagen(pantalla_config["pokebola"])
    
    dibujar_cartas(pantalla_config["carta_1"],pantalla_config["carta_2"])

def mostrar_cartas(diccionario, pantalla, colores, coordenadas_texto, escala_poke_imagen, coordenas_imagen):#!
    """
    Descripción: Muestra los datos de un Pokémon junto con su imagen en pantalla.

    Args:
        diccionario (dict): Diccionario con los datos del Pokémon.
        pantalla (Surface): Superficie de Pygame donde se dibuja la información y las imágenes.
        colores (dict): Diccionario de colores para los textos.
        coordenadas_texto (tuple): Coordenadas (x, y) para posicionar el texto.
        escala_poke_imagen (tuple): Escala (ancho, alto) de la imagen.
        coordenas_imagen (tuple): Coordenadas (x, y) de la imagen.
    """
    y = coordenadas_texto[1]

    for clave, atributo in diccionario.items():
        clave_del_pokemon = f"{clave}: "
        atributo_del_pokemon = f" {atributo}"
        y += 40
        texto_a = generar_texto_renderizado(pantalla, ("Arial", 20), clave_del_pokemon, colores["negro"], (coordenadas_texto[0], y), colores["dorado"])
        texto_b = generar_texto_renderizado(pantalla, ("Arial", 20), atributo_del_pokemon, colores["negro"], (591, y), colores["verde"])

        if clave != "poke-foto":
            dibujar_texto(texto_a)
            dibujar_texto(texto_b)
        else:
            mostrar_foto_pokemon(pantalla, atributo, escala_poke_imagen, coordenas_imagen)

def mostrar_foto_pokemon(pantalla, pokemon, escala_poke_imagen, coordenas_imagen):
    """
    Descripción: Muestra la imagen de un Pokémon en la pantalla.

    Args:
        pantalla (Surface): Superficie donde se dibuja la imagen.
        pokemon (str): Ruta de la imagen del Pokémon.
        escala_poke_imagen (tuple): Escala (ancho, alto) de la imagen.
        coordenas_imagen (tuple): Coordenadas (x, y) de la imagen.
    """
    ventana = pantalla["ventana"]
    
    imagen_final = crear_diccionario_imagen(ventana, pokemon, coordenas_imagen, escala_poke_imagen)
    
    dibujar(imagen_final, dibujar_imagen)

def actualizar():
    """
    Descripción: Actualiza la pantalla con los cambios realizados.

    """
    pygame.display.update()

def mostrar_texto(pantalla, fuente, texto_escrito, color_texto, posicion, color_fondo_texto):
    """
    Descripción: Muestra texto en la ventana.

    Args:
        pantalla (Surface): Superficie donde se muestra el texto.
        fuente (tuple): Tipo y tamaño de fuente.
        texto_escrito (str): Texto que se va a mostrar.
        color_texto (tuple): Color del texto.
        posicion (tuple): Coordenadas (x, y) para la posición del texto.
        color_fondo_texto (tuple): Color de fondo del texto (opcional).
    """
    texto = generar_texto_renderizado(pantalla, fuente, texto_escrito, color_texto, posicion, color_fondo_texto)
    
    dibujar(texto, dibujar_texto)

def obtener_tiempo(tiempo_actual, tiempo_inicial):
    """
    Descripción: Calcula el tiempo transcurrido en segundos.

    Args:
        tiempo_actual (int): Tiempo actual en milisegundos.
        tiempo_inicial (int): Tiempo inicial en milisegundos.

    Returns:
        str: Tiempo transcurrido formateado como string con dos decimales (en segundos).
    """
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_transcurrido = f"{(tiempo_transcurrido * 0.001):.02f}"  # Convertir milisegundos a segundos.
    tiempo_transcurrido = str(tiempo_transcurrido)

    return tiempo_transcurrido

def mostrar_cronometro(pantalla:dict, cronometro_activo:bool, tiempo_inicial:int, colores:dict):
    """
    Descripción: Muestra el cronómetro en la ventana si está activo.

    Args:
        pantalla (dict): Diccionario con los datos de la pantalla.
        cronometro_activo (bool): Indica si el cronómetro está funcionando.
        tiempo_inicial (int): Tiempo inicial del cronómetro.
        colores (dict): Diccionario de colores, usado para definir el color del texto del cronómetro.
    """
    if cronometro_activo:
        tiempo_actual = pygame.time.get_ticks()

        tiempo_transcurrido = obtener_tiempo(tiempo_actual, tiempo_inicial)

        tiempo_final = generar_texto_renderizado(pantalla, ("Arial", 25), tiempo_transcurrido, colores["negro"], (58, 414), colores["rosa"])

        dibujar(tiempo_final, dibujar_texto)

def mostrar_pantalla_inicio(boton:dict, pantalla_config:dict, colores:dict):
    """
    Descripción: Muestra la pantalla de inicio con el botón centrado.

    Args:
        boton (dict): Botón para iniciar el juego.
        pantalla_config (dict): Configuración de la pantalla, como la superficie y los colores.
        colores (dict): Diccionario de colores para los elementos visuales.
    """
    dibujar_fondo(pantalla_config, True)
    dibujar_texto_centralizado(boton, colores)
    actualizar()

def verificar_existencia_de_nombres(datos:dict, boton:dict, boton_1:dict, boton_2:dict, colores:dict):
    """
    Descripción: Verifica que se hayan ingresado los nombres de los jugadores, en caso contrario,
    se tomará que no se desea jugar.

    Args:
        datos (dict): Información de los datos del juego.
        boton (dict): Botón de iniciar juego.
        boton_1 (dict): Primer botón para ingresar nombre.
        boton_2 (dict): Segundo botón para ingresar nombre.
        colores (dict): Diccionario de donde sacamos los datos.

    Returns:
        list: Lista con los nombres ingresados o un valor `None` si no se desea jugar.
    """
    verificar_textboxs = manejador_pedir_nombres(datos, boton_1, boton_2, colores)

    if verificar_textboxs == None:
        datos["primer_pantalla"] = False
        datos["empezar_juego"] = False
        datos["bandera_principal"] = False
        lista = [None]
        
    elif verificar_textboxs[0]:
        lista = [verificar_textboxs[1], verificar_textboxs[2]]
        manejador_cerrar_pantalla(datos, boton)

    return lista

def verificar_nombre_valido(boton:dict):
    """
    Descripción: Verifica si el nombre ingresado en el botón es válido (tiene al menos 3 caracteres).

    Args:
        boton (dict): Botón que contiene el texto del nombre.

    Returns:
        bool: `True` si el nombre es válido, `False` si no lo es.
    """
    hay_nombre_valido = None
    if boton["activo"] == False:
        longitud = len(boton["texto"])
        if longitud >= 3:
            hay_nombre_valido = True
        else:
            hay_nombre_valido = False

    return hay_nombre_valido

def guardar_nombres_usuarios(nombre_registrado, nombre_registrado_2, boton_1, boton_2)->list:
    """
    Descripción: Guarda los nombres de los jugadores si ambos son válidos.

    Args:
        nombre_registrado (bool): Indica si el primer nombre es válido.
        nombre_registrado_2 (bool): Indica si el segundo nombre es válido.
        boton_1 (dict): Botón con el primer nombre.
        boton_2 (dict): Botón con el segundo nombre.

    Returns:
        list: con nombres, o con un bool.
    """
    lista = [False]
    if nombre_registrado == True and nombre_registrado_2 == True:
        lista.clear()
        lista.append(True)
        lista.append(boton_1["texto"])
        lista.append(boton_2["texto"])
    
    return lista

def manejador_cerrar_pantalla(datos, boton):
    """
    Descripción: Maneja la interacción de cerrar la pantalla al hacer clic en el botón correspondiente.

    Args:
        datos (dict): Datos de la configuración del juego, como la pantalla activa y el estado del juego.
        boton (dict): El botón que, al ser presionado, cierra la pantalla de inicio.
    """
    while datos["primer_pantalla"]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                datos["primer_pantalla"] = False
                datos["empezar_juego"] = False
                datos["bandera_principal"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton["cuadrado"].collidepoint(evento.pos):
                    datos["primer_pantalla"] = False

def manejador_pedir_nombres(datos, boton_1, boton_2, colores):
    """
    Descripción: Maneja la interacción de pedir los nombres de los jugadores. Permite escribir y modificar los nombres
    de los jugadores 1 y 2, y valida que ambos sean válidos antes de continuar.

    Args:
        datos (dict): Datos de la configuración del juego y estado de la pantalla.
        boton_1 (dict): El primer botón para ingresar el nombre del jugador 1.
        boton_2 (dict): El segundo botón para ingresar el nombre del jugador 2.
        colores (dict): Colores usados para el texto y los elementos gráficos.

    Returns:
        list: Lista con los nombres de los jugadores si ambos son válidos, `None` si no lo son.
    """
    lista_de_botones = [boton_1, boton_2]
    nombre_registrado = None
    nombre_registrado_2 = None

    while datos["primer_pantalla"]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                datos["primer_pantalla"] = False
                datos["empezar_juego"] = False
                datos["bandera_principal"] = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                detectar_cambio_color(lista_de_botones, evento)
            elif evento.type == pygame.KEYDOWN:
                if boton_1["activo"]:
                    detectar_escritura(boton_1, evento)
                elif boton_2["activo"]:
                    detectar_escritura(boton_2, evento)

                nombre_registrado = verificar_nombre_valido(boton_1)
                nombre_registrado_2 = verificar_nombre_valido(boton_2)

        dibujar_texto_centralizado(boton_1, colores)
        dibujar_texto_centralizado(boton_2, colores)
        actualizar()

        lista = guardar_nombres_usuarios(nombre_registrado, nombre_registrado_2, boton_1, boton_2)

        if lista[0] != False:
            return lista

def cargar_pantalla_inicial(bandera_principal, pantalla_config, elementos_juego, ventana, colores, parametros) -> list:
    """
    Descripción: Carga la pantalla inicial del juego, mostrando los botones para ingresar los nombres y comenzar el juego.

    Args:
        bandera_principal (bool): Indica si el juego debe comenzar.
        pantalla_config (dict): Configuración de la pantalla, como la superficie y los colores.
        elementos_juego (dict): Elementos del juego como los botones y los cuadros de texto.
        ventana (Surface): La ventana principal de Pygame donde se dibujarán los elementos.
        colores (dict): Colores para los textos, botones y fondos.
        parametros (dict): Parámetros adicionales para configurar el juego (si aplica).

    Returns:
        list: Lista con los resultados del inicio del juego (si se ha comenzado o no).
    """
    empezar_juego = True
    primer_pantalla = True

    datos = crear_banderas_pantalla_inicial(ventana, primer_pantalla, empezar_juego, bandera_principal)
    boton_comenzar = crear_cuadrado(ventana, colores["blanco"], (825, 189), (200, 60), ("Arial", 20), "COMENZAR")
    boton_nombre_uno = crear_boton(ventana, ("Arial", 20), colores, (1115, 27), (175, 60), escribir_teclado, None, "")
    boton_nombre_dos = crear_boton(ventana, ("Arial", 20), colores, (1115, 101), (175, 60), escribir_teclado, None, "")

    while primer_pantalla:
        mostrar_pantalla_inicio(boton_comenzar, pantalla_config, colores)
        jugadores_nombre = verificar_existencia_de_nombres(datos, boton_comenzar, boton_nombre_uno, boton_nombre_dos, colores)

        primer_pantalla = datos["primer_pantalla"]
        empezar_juego = datos["empezar_juego"]
        bandera_principal = datos["bandera_principal"]

        actualizar()

    lista = chequear_nombres(jugadores_nombre, empezar_juego, bandera_principal)

    if bandera_principal != False or empezar_juego != False:
        iniciar_partida(pantalla_config, elementos_juego, jugadores_nombre, colores)

    return lista

def chequear_nombres(jugadores_nombre, empezar_juego, bandera_principal):
    """
    Descripción: Verifica si los jugadores tienen nombres válidos antes de comenzar el juego.

    Args:
        jugadores_nombre (list): Lista con los nombres de los jugadores.
        empezar_juego (bool): Indica si el juego debe comenzar.
        bandera_principal (bool): Indica si la bandera principal está activa.

    Returns:
        list: Lista con la información sobre el estado del juego y los nombres de los jugadores si son válidos.
    """
    lista = [empezar_juego, bandera_principal, None, None]

    if jugadores_nombre[0] != None:
        lista = [empezar_juego, bandera_principal, jugadores_nombre[0], jugadores_nombre[1]]

    return lista

def iniciar_partida(pantalla_config, elementos_juego, jugadores_nombre, colores):
    """
    Descripción: Inicia el juego configurando la pantalla, los elementos gráficos y los jugadores.

    Args:
        pantalla_config (dict): Configuración de la pantalla, como la superficie y colores.
        elementos_juego (dict): Elementos gráficos y objetos del juego.
        jugadores_nombre (list): Lista con los nombres de los jugadores.
        colores (dict): Colores para los elementos gráficos y textos.
    """
    setear_pantalla(pantalla_config, elementos_juego, jugadores_nombre, colores)
    actualizar()
