import pygame

def dibujar(diccionario:dict,tipo_dibujo):
    """Descripcion: Dibuja el elemento que se le pase por parametro junto con su respectivo orden.

    Args:
        diccionario (dict): diccionario de donde se sacan los datos
        tipo_dibujo (_type_): funcion que dibujara los elementos del diccionario
    """

    tipo_dibujo(diccionario)

def dibujar_cuadrados_con_textos(lista_cuadrados):
    for input in lista_cuadrados:
        dibujar_cuadrado_con_texto(input)

def dibujar_boton_musical(boton):
    boton["ventana"].blit(boton["contenido"], boton["posicion"])

def dibujar_botones(lista):
    for boton in lista:
        dibujar_boton_musical(boton)

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

def dibujar_fondo(pantalla_config,fondo_principal=None):
    if fondo_principal != None:
        pantalla_config["ventana"].blit(pantalla_config["fondo"],(0,0))
    else:
        pantalla_config["ventana"].blit(pantalla_config["fondo_2"],(0,0))

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

def dibujar_rectangulo_cartas(carta_1,carta_2):
    """
    Dibuja dos rectángulos que representan cartas.

    Args:
        carta_1 (dict): Diccionario de la primera carta.
        carta_2 (dict): Diccionario de la segunda carta.
    """
    dibujar(carta_1,dibujar_cuadrados)
    dibujar(carta_2,dibujar_cuadrados)

def mostrar_texbox_pantalla(input):
    superficie = input["fuente"].render(input["texto"],False,"Black")
    input["ventana"].blit(superficie,(input["cuadrado"].x+5,input["cuadrado"].y+7))
    pygame.draw.rect(input["ventana"],input["color_actual"],input["cuadrado"],2)