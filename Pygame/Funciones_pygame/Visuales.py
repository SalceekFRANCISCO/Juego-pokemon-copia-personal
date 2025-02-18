import pygame
from Funciones_pygame.Dibujo import *

# def setear_accion_pantalla(accion):
#     if accion != None and accion["bandera"] == True:
#         dibujar_solo_texto(accion["texto_pantalla"])

# def setear_acciones_pantalla(acciones):
#     for accion in acciones:
#         if accion != "vacio":        
#             dibujar_solo_texto(accion["texto_pantalla"])

def setear_accion_pantalla(accion):
    if accion != None:
        if accion["bandera"]:
            dibujar_solo_texto(accion["texto_pantalla"])

def setear_acciones_pantalla(accion_a,accion_b):
        setear_accion_pantalla(accion_a)

        setear_accion_pantalla(accion_b)            

def setear_pantalla(pantalla_config,elementos_juego,colores):#! va a necesitar ambos diccionarios

    dibujar(pantalla_config,rellenar_superficie)

    dibujar(elementos_juego["boton_nombre_uno"],mostrar_texbox_pantalla)
    dibujar(elementos_juego["boton_nombre_dos"],mostrar_texbox_pantalla)

    dibujar_lista_cuadrados(pantalla_config["lista_cuadrados"])

    dibujar_cuadrado_con_texto(elementos_juego["boton_jugar"])
    dibujar_cuadrado_con_texto(elementos_juego["ganador_partida"])
    dibujar_cuadrado_con_texto(elementos_juego["atributo"])

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

def generar_texto_renderizado (pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto):#! ventana
    texto = {}
    texto["ventana"] = pantalla["ventana"]
    texto["texto_escrito"] = renderizar_mensaje((fuente[0],fuente[1]),texto_escrito,color_texto,color_fondo_texto)
    texto["posicion"] = posicion

    return texto

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

def renderizar_mensaje(fuente:tuple, mensaje: str, color_texto: tuple,color_fondo_texto):
    fuente_creada = crear_fuente(fuente[0],fuente[1])
    texto_definitivo = renderizar_texto(fuente_creada,mensaje,color_texto,color_fondo_texto)

    return texto_definitivo

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

def mostrar_texbox_pantalla(input):
    superficie = input["fuente"].render(input["texto"],False,"Black")
    input["ventana"].blit(superficie,(input["cuadrado"].x+5,input["cuadrado"].y+7))
    pygame.draw.rect(input["ventana"],input["color_actual"],input["cuadrado"],2)

#region cosas que no se usan

#? Esta funcion es de modelo para las otras
# def dibujar(input):
#     """
#     Dibuja un campo de texto con un rectángulo y el texto que contiene.

#     Args:
#         input (dict): Diccionario del campo de texto.
#     """
#     superficie = input["fuente"].render(input["texto"],False,"Black")
#     input["ventana"].blit(superficie,input["rectangulo"])
#     pygame.draw.rect(input["ventana"], input["color_actual"], input["rectangulo"],2)


#? Esta funcion es de modelo para las otras
# def dibujar_rectangulo(ventana, color, boton):
#     """
#     Dibuja un rectángulo en la ventana.

#     Args:
#         ventana (Surface): Superficie de Pygame donde se dibuja el rectángulo.
#         color (tuple): Color del rectángulo en formato RGB.
#         boton (Rect): Objeto Rect de Pygame que representa el rectángulo.
#     """
#     pygame.draw.rect(ventana, color, boton)



#endregion