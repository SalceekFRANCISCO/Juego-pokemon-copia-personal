import pygame
from Funciones_pygame.Dibujo import *
from Funciones_pygame.Interaccion import *

def setear_acciones_pantalla_ses(acciones):
    if acciones != None:
        for accion in acciones:
            if accion != None:        
                dibujar_solo_texto(accion["texto_pantalla"])

def setear_accion_pantalla(accion):
    if accion != None and accion["bandera"]:
        # if accion["bandera"]:
            dibujar_solo_texto(accion["texto_pantalla"])

def setear_acciones_pantalla(accion_a,accion_b):
        setear_accion_pantalla(accion_a)

        setear_accion_pantalla(accion_b)            

def setear_pantalla(pantalla_config,elementos_juego):#! va a necesitar ambos diccionarios

    dibujar(pantalla_config,rellenar_superficie)

    dibujar(elementos_juego["boton_nombre_uno"],mostrar_texbox_pantalla)
    dibujar(elementos_juego["boton_nombre_dos"],mostrar_texbox_pantalla)

    dibujar(elementos_juego["lista_botones_musicales"],dibujar_botones)

    dibujar_lista_cuadrados(pantalla_config["lista_cuadrados"])

    dibujar_cuadrado_con_texto(elementos_juego["boton_jugar"])
    dibujar_cuadrado_con_texto(elementos_juego["atributo"])
    dibujar_cuadrado_con_texto(elementos_juego["ganador_ronda"])
    dibujar_cuadrado_con_texto(elementos_juego["ganador_partida"])

    dibujar_imagenes(pantalla_config["pokebola"])
    
    dibujar_rectangulo_cartas(pantalla_config["carta_1"],pantalla_config["carta_2"])

def mostrar_cartas(diccionario, ventana, colores, coordenadas_texto, escala_poke_imagen, coordenas_imagen):
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
        pokemon = f"{clave}: {atributo}"
        texto = renderizar_mensaje(("Arial",20),pokemon,colores["negro"],colores["gris"])
        y += 40
        if clave != "poke-foto":
            dibujar_pantalla(ventana,texto,(coordenadas_texto[0],y))
        else:
            mostrar_foto_pokemon(ventana,atributo,escala_poke_imagen,coordenas_imagen)

def mostrar_foto_pokemon(ventana, pokemon:str, escala_poke_imagen: tuple, coordenas_imagen: tuple):
    """
    Muestra la imagen de un Pokémon en la pantalla.

    Args:
        ventana (Surface): Superficie donde se dibuja la imagen.
        pokemon (str): Ruta de la imagen del Pokémon.
        escala_poke_imagen (tuple): Escala (ancho, alto) de la imagen.
        coordenas_imagen (tuple): Coordenadas (x, y) de la imagen.
    """

    imagen_final = crear_diccionario_imagen(ventana,pokemon,coordenas_imagen,escala_poke_imagen)
    
    dibujar(imagen_final,dibujar_imagenes)

def actualizar():
    """
    Actualiza la pantalla con los cambios realizados.
    """
    pygame.display.update()

def mostrar_texto(pantalla, fuente, texto_escrito, color_texto, posicion,color_fondo_texto):#! ventana
    """
    Muestra texto en la ventana.

    Args:
        ventana (Surface): Superficie donde se muestra el texto.
        fuente (tuple): Tipo y tamaño de fuente.
        texto_escrito (str): Texto a mostrar.
        color_texto (tuple): Color del texto en formato RGB.
        posicion (tuple): Coordenadas (x, y) para el texto.
    """
    texto = generar_texto_renderizado (pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto)

    dibujar(texto,dibujar_solo_texto)

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

def mostrar_cronometro(pantalla, cronometro_activo, tiempo_inicial, colores):#! ventana
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

        # Crear el temporizador con el tiempo transcurrido
        tiempo_final = crear_temporizador(pantalla["ventana"], ("Arial", 20), (58, 414), (200, 32), tiempo_transcurrido, colores["negro"])

        # Mostrar el tiempo en pantalla
        dibujar(tiempo_final,dibujar_tiempo)
