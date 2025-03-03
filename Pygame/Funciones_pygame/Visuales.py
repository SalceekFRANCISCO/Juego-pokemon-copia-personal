import pygame
from Funciones_pygame.Dibujo import *
from Funciones_pygame.Interaccion import *
#region
#endregion

def setear_pantalla(pantalla_config,elementos_juego,jugadores,colores):

    dibujar_fondo(pantalla_config)

    dibujar(elementos_juego["lista_botones_musicales"],dibujar_botones_musicales)

    dibujar(pantalla_config["lista_cuadrados"],dibujar_lista_cuadrados)

    mostrar_texto(pantalla_config,("Arial",30),jugadores[0],colores["negro"],(795,40),colores["rosa"])
    mostrar_texto(pantalla_config,("Arial",30),jugadores[1],colores["negro"],(797,623),colores["rosa"])

    dibujar_textos_en_cuadrados(elementos_juego["lista_rect_texto"],colores)

    dibujar_imagen(pantalla_config["pokebola"])
    
    dibujar_cartas(pantalla_config["carta_1"],pantalla_config["carta_2"])

def mostrar_cartas(diccionario, pantalla, colores, coordenadas_texto, escala_poke_imagen, coordenas_imagen):#!revisar
    """
    Descripcion: Muestra los datos de un Pokémon junto con su imagen en pantalla.

    Args:
        diccionario (dict): Diccionario con los datos del Pokémon.
        ventana (Surface): Superficie de Pygame donde se dibuja.
        colores (dict): Diccionario de colores.
        coordenadas_texto (tuple): Coordenadas para mostrar el texto.
        escala_poke_imagen (tuple): Escala (ancho, alto) de la imagen.
        coordenas_imagen (tuple): Coordenadas (x, y) de la imagen.
    """
    
    y = coordenadas_texto[1]

    for clave, atributo in diccionario.items():
        clave_del_pokemon = f"{clave}: "
        atributo_del_pokemon = f" {atributo}"
        y += 40
        texto_a = generar_texto_renderizado(pantalla,("Arial",20),clave_del_pokemon,colores["negro"],(coordenadas_texto[0],y),colores["dorado"])
        texto_b = generar_texto_renderizado(pantalla,("Arial",20),atributo_del_pokemon,colores["rojo"],(591,y),colores["verde"])

        if clave != "poke-foto":
            dibujar_texto(texto_a)
            dibujar_texto(texto_b)
        else:
            mostrar_foto_pokemon(pantalla,atributo,escala_poke_imagen,coordenas_imagen)

def mostrar_foto_pokemon(pantalla, pokemon:str, escala_poke_imagen: tuple, coordenas_imagen: tuple):
    """
    Muestra la imagen de un Pokémon en la pantalla.

    Args:
        ventana (Surface): Superficie donde se dibuja la imagen.
        pokemon (str): Ruta de la imagen del Pokémon.
        escala_poke_imagen (tuple): Escala (ancho, alto) de la imagen.
        coordenas_imagen (tuple): Coordenadas (x, y) de la imagen.
    """
    ventana = pantalla["ventana"]
    
    imagen_final = crear_diccionario_imagen(ventana,pokemon,coordenas_imagen,escala_poke_imagen)
    
    dibujar(imagen_final,dibujar_imagen)

def actualizar():
    """
    Actualiza la pantalla con los cambios realizados.
    """
    pygame.display.update()

def mostrar_texto(pantalla, fuente, texto_escrito, color_texto, posicion,color_fondo_texto):
    """
    Muestra texto en la ventana.

    Args:
        ventana (Surface): Superficie donde se muestra el texto.
        fuente (tuple): Tipo y tamaño de fuente.
        texto (str): Texto a mostrar.
        color_texto (tuple): Color del texto en formato RGB.
        posicion (tuple): Coordenadas (x, y) para el texto.
    """
    texto = generar_texto_renderizado(pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto)

    dibujar(texto,dibujar_texto)

def obtener_tiempo(tiempo_actual, tiempo_inicial):
    """
    Calcula el tiempo transcurrido en segundos.

    Args:
        tiempo_actual (int): Tiempo actual en milisegundos.
        tiempo_inicial (int): Tiempo inicial en milisegundos.

    Returns:
        str: Tiempo transcurrido formateado como string.
    """
    tiempo_transcurrido = tiempo_actual - tiempo_inicial 
    # print(f"{(tiempo_transcurrido*0.001):.02f}")
    tiempo_transcurrido = f"{(tiempo_transcurrido*0.001):.02f}"#milisegundos a segundos,
    tiempo_transcurrido = str(tiempo_transcurrido)

    return tiempo_transcurrido

def mostrar_cronometro(pantalla, cronometro_activo, tiempo_inicial, colores):
    """
    Muestra un cronómetro en la ventana si está activo.

    Args:
        pantalla (dict): Diccionario con los datos de la pantalla.
        cronometro_activo (bool): Indica si el cronómetro está funcionando.
        tiempo_inicial (int): Tiempo inicial del cronómetro.
        colores (dict): Diccionario de colores.
    """
    
    if cronometro_activo:
        # Obtener el tiempo actual
        tiempo_actual = pygame.time.get_ticks()

        # Calcular el tiempo transcurrido desde que empezó el cronómetro
        tiempo_transcurrido = obtener_tiempo(tiempo_actual, tiempo_inicial)

        tiempo_final = generar_texto_renderizado(pantalla, ("Arial", 25),tiempo_transcurrido, colores["negro"],(58, 414), colores["rosa"])

        dibujar(tiempo_final,dibujar_texto)

def cargar_pantalla_inicio(datos:dict,boton,boton_1,boton_2,pantalla_config,colores):

    dibujar_fondo(pantalla_config,True)
    dibujar_texto_centralizado(boton,colores)
    actualizar()

    lista_jugadores = verificar_existencia_de_nombres(datos,boton,boton_1,boton_2,colores)

    return lista_jugadores

def verificar_existencia_de_nombres(datos,boton,boton_1,boton_2,colores): #! TRABAJAR
    verificacion_textboxs = manejador_pedir_nombres(datos,boton_1,boton_2,colores)

    if verificacion_textboxs == None or verificacion_textboxs[0] == False:
        datos["primer_pantalla"] = False
        datos["empezar_juego"] = False
        datos["bandera_principal"] = False
        lista = [None]

    elif verificacion_textboxs[0]:
        manejador_cerrar_pantalla(datos,boton)
        lista = [verificacion_textboxs[1],verificacion_textboxs[2]]

    return lista

def verificar_nombre_valido(boton):
    hay_nombre_valido = None
    if boton["activo"] == False:
        longitud = len(boton["texto"])
        if longitud >= 3:
            hay_nombre_valido = True
        else:
            hay_nombre_valido = False

    return hay_nombre_valido

def guardar_nombres_usuarios(nombre_registrado,nombre_registrado_2,boton_1,boton_2):
    lista = [False]
    if nombre_registrado == True and nombre_registrado_2 == True:
        lista.clear()
        lista.append(True)
        lista.append(boton_1["texto"])
        lista.append(boton_2["texto"])
    
    return lista

def manejador_cerrar_pantalla(datos:dict,boton:dict):
    while datos["primer_pantalla"]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                datos["primer_pantalla"] = False
                datos["empezar_juego"] = False
                datos["bandera_principal"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton["cuadrado"].collidepoint(evento.pos):
                    datos["primer_pantalla"] = False

def manejador_pedir_nombres(datos,boton_1,boton_2,colores):#! TRABAJAR
    lista_de_botones = [boton_1,boton_2]
    nombre_registrado = None
    nombre_registrado_2 = None

    while datos["primer_pantalla"]:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                datos["primer_pantalla"] = False
                datos["empezar_juego"] = False
                datos["bandera_principal"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                detectar_cambio_color(lista_de_botones,evento)

            elif evento.type == pygame.KEYDOWN:
                if boton_1["activo"]:
                    detectar_escritura(boton_1,evento)

                elif boton_2["activo"]:
                    detectar_escritura(boton_2,evento)

                nombre_registrado = verificar_nombre_valido(boton_1)

                nombre_registrado_2 = verificar_nombre_valido(boton_2)

        dibujar_texto_centralizado(boton_1,colores)
        dibujar_texto_centralizado(boton_2,colores)
        actualizar()
        
        lista = guardar_nombres_usuarios(nombre_registrado,nombre_registrado_2,boton_1,boton_2)

        if lista[0] != False:

            return lista

def pantalla_inicial(bandera_principal,pantalla_config,elementos_juego,ventana,colores,parametros)->list:#! TRABAJAR
    empezar_juego = True
    primer_pantalla = True

    datos = crear_banderas_pantalla_inicial(ventana,primer_pantalla,empezar_juego,bandera_principal)

    boton_comenzar = crear_cuadrado(ventana,colores["blanco"],(825,189),(200,60),("Arial",20),"COMENZAR")
    boton_nombre_uno = crear_boton(ventana,("Arial",20),colores,(1115,27),(175,60),procesar_entrada_texto,parametros[1],"")
    boton_nombre_dos = crear_boton(ventana,("Arial",20),colores,(1115,101),(175,60),procesar_entrada_texto,parametros[2],"")

    while primer_pantalla:
        jugadores_nombre = cargar_pantalla_inicio(datos,boton_comenzar,boton_nombre_uno,boton_nombre_dos,pantalla_config,colores)
        
        primer_pantalla = datos["primer_pantalla"]
        empezar_juego = datos["empezar_juego"]
        bandera_principal = datos["bandera_principal"]

        actualizar()

    if bandera_principal != False or empezar_juego != False:
        setear_pantalla(pantalla_config,elementos_juego,jugadores_nombre,colores)
        actualizar()

    if jugadores_nombre[0] == None:
        lista = [empezar_juego, bandera_principal,None,None]
    else:
        lista = [empezar_juego, bandera_principal,jugadores_nombre[0],jugadores_nombre[1]]


    return lista