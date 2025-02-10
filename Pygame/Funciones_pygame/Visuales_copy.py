import pygame
# from Logica.Consola_2_FG import *
# from Funciones_pygame.Dicc_interaccion import *

#! para las funciones que reciben colores me gustaría, que se pase el diccionario y el color puntual
#! para que busque esa clave en ese diccionario

#region (solo dibujar)
def dibujar(diccionario:dict,tipo_dibujo):#? me encanta
    """Descripcion: Dibuja el elemento que se le pase por parametro junto con su respectivo orden.

    Args:
        diccionario (dict): diccionario de donde se sacan los datos
        tipo_dibujo (_type_): funcion que dibujara los elementos del diccionario
    """

    tipo_dibujo(diccionario)

def dibujar_cuadrados(cuadrado:dict):
    """
    Dibuja un cuadrado en la ventana.

    Args:
        cuadrado (dict): Diccionario con los datos del cuadrado.
    """
    pygame.draw.rect(cuadrado["ventana"], cuadrado["color_actual"], cuadrado["cuadrado"])

def dibujar_solo_texto(texto:dict):
    """Muestra solo texto en la ventana.

    Args:
        texto (dict): Diccionario con datos del texto.
    """
    texto["ventana"].blit(texto["texto_escrito"],texto["posicion"])

def dibujar_tiempo(tiempo_final:dict):
    """
    Muestra el tiempo en la ventana.

    Args:
        tiempo_final (dict): Diccionario con datos del temporizador.
    """
    tiempo_final["ventana"].blit(tiempo_final["texto"],(tiempo_final["rectangulo"].x, tiempo_final["rectangulo"].y))

def dibujar_imagenes(imagen:dict):
    """
    Dibuja una imagen en la ventana en sus coordenadas asignadas.

    Args:
        imagen (dict): Diccionario con los datos de la imagen.
    """
    imagen["ventana"].blit(imagen["imagen_final"],imagen["coordenadas"])

def rellenar_superficie(pantalla:dict):
    """
    Llena toda la superficie de la ventana con un color.

    Args:
        ventana (Surface): Superficie de Pygame que se llena.
        color (tuple): Color en formato RGB.
    """
    pantalla["ventana"].fill(pantalla["color_ventana"])
#endregion
############################################################# 

#region dibujar
########################### DIBUJAR ########################### 
def setear_pantalla(pantalla,colores):
    """
    Configura y dibuja los elementos principales en la pantalla.

    Args:
        pantalla (dict): Diccionario con los datos de la pantalla.
        colores (dict): Diccionario de colores para la interfaz.
    """

    dibujar(pantalla,rellenar_superficie)

    dibujar(pantalla["boton_nombre_uno"],mostrar_texbox_pantalla)
    dibujar(pantalla["boton_nombre_dos"],mostrar_texbox_pantalla)

    dibujar_lista_cuadrados(pantalla["lista_cuadrados"])

    dibujar_cuadrado_con_texto(pantalla["boton_jugar"])
    dibujar_cuadrado_con_texto(pantalla["ganador_partida"])
    dibujar_cuadrado_con_texto(pantalla["atributo"])

    if pantalla["reemplazo_boton"]:
        dibujar_cuadrado_con_texto(pantalla["boton_reinicio"])
        pantalla["boton_reinicio"]["color_actual"] = colores["blanco"]

    dibujar_imagenes(pantalla["pokebola"])
    
    dibujar_rectangulo_cartas(pantalla["carta_1"],pantalla["carta_2"])

def dibujar_pantalla(ventana, elemento, coordenadas:tuple):
    """
    Dibuja un elemento en la ventana en las coordenadas especificadas.

    Args:
        ventana (Surface): Superficie de Pygame donde se dibuja el elemento.
        elemento (Surface): Elemento a dibujar.
        coordenadas (tuple): Coordenadas (x, y) para dibujar el elemento.
    """
    ventana.blit(elemento,coordenadas)

def dibujar_lista_cuadrados(lista_cuadrados:list):
    """
    Dibuja una lista de cuadrados en la pantalla.

    Args:
        lista_cuadrados (list): Lista de diccionarios que representan los cuadrados.

    Returns:
        dict: Último cuadrado dibujado de la lista.
    """
    for cuadrado in lista_cuadrados:
        dibujar_cuadrados(cuadrado)

def dibujar_rectangulo_cartas(carta_1,carta_2):
    """
    Dibuja dos rectángulos que representan cartas.

    Args:
        carta_1 (dict): Diccionario de la primera carta.
        carta_2 (dict): Diccionario de la segunda carta.
    """
    dibujar(carta_1,dibujar_cuadrados)
    dibujar(carta_2,dibujar_cuadrados)

def dibujar_cuadrado_con_texto(input):
    """
    Dibuja un botón rectangular con un texto centrado.

    Args:
        input (dict): Diccionario con los datos del botón.
    """
    superficie = input["fuente"].render(input["texto"], True, "Black")
    
    rectangulo_texto = superficie.get_rect(center=input["cuadrado"].center)
    
    dibujar(input,dibujar_cuadrados)
    
    dibujar_pantalla(input["ventana"],superficie,rectangulo_texto.topleft)

def mostrar_texbox_pantalla(input):
    superficie = input["fuente"].render(input["texto_escritura"],False,"Black")
    input["ventana"].blit(superficie,(input["cuadrado"].x+5,input["cuadrado"].y + 7))
    pygame.draw.rect(input["ventana"],input["color_actual"],input["cuadrado"],2)

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

#endregion
############################################################# 

#region texto 
########################### TEXTO ########################### 

def crear_diccionario_texto(pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto):
    texto = {}
    texto["ventana"] = pantalla["ventana"]
    texto["texto_escrito"] = renderizar_mensaje((fuente[0],fuente[1]),texto_escrito,color_texto,color_fondo_texto)
    texto["posicion"] = posicion

    return texto

def mostrar_texto(pantalla, fuente, texto_escrito, color_texto, posicion,color_fondo_texto):
    """
    Muestra texto en la ventana.

    Args:
        ventana (Surface): Superficie donde se muestra el texto.
        fuente (tuple): Tipo y tamaño de fuente.
        texto_escrito (str): Texto a mostrar.
        color_texto (tuple): Color del texto en formato RGB.
        posicion (tuple): Coordenadas (x, y) para el texto.
    """
    texto = crear_diccionario_texto(pantalla,fuente,texto_escrito,color_texto,posicion,color_fondo_texto)

    dibujar(texto,dibujar_solo_texto)

def renderizar_mensaje(fuente:tuple, mensaje: str, color_texto: tuple,color_fondo_texto):
    fuente_creada = crear_fuente(fuente[0],fuente[1])
    texto_definitivo = renderizar_texto(fuente_creada,mensaje,color_texto,color_fondo_texto)

    return texto_definitivo

#endregion
############################################################# 

#region imagenes 
########################### IMAGENES ########################### 
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

#endregion
############################################################# 

#region tiempo 
########################### TIEMPO ########################### 
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

        # Crear el temporizador con el tiempo transcurrido
        tiempo_final = crear_temporizador(pantalla["ventana"], ("Arial", 20), (58, 414), (200, 32), tiempo_transcurrido, colores["negro"])

        # Mostrar el tiempo en pantalla
        dibujar(tiempo_final,dibujar_tiempo)

#endregion
############################################################# 

#region funciones pequeñas/individuales 

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

def actualizar():
    """
    Actualiza la pantalla con los cambios realizados.
    """
    pygame.display.update()

#endregion
############################################################# 

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
############################################################# 