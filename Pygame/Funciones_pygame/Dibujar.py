import pygame

def dibujar(diccionario:dict,tipo_dibujo):
    """Descripcion: Dibuja el elemento que se le pase por parametro junto con su respectivo orden.

    Args:
        diccionario (dict): diccionario de donde se sacan los datos
        tipo_dibujo (_type_): funcion que dibujara los elementos del diccionario
    """

    tipo_dibujo(diccionario)

def dibujar_textos_en_cuadrados(lista_cuadrados,colores):
    """Descripción: Dibuja texto en los respectivos cuadrados.

    Args:
        lista_cuadrados (list): lista de cuadrados
        colores (dict): diccionario de colores
    """
    for input in lista_cuadrados:
        dibujar_texto_centralizado(input,colores)

def dibujar_botones_musicales(lista:list):
    """Descripción: dibuja los botones de la lista musical.

    Args:
        lista (list): lista de botones musicales.
    """
    for boton in lista:
        dibujar_boton_musical(boton)

def dibujar_lista_cuadrados(lista_cuadrados:list):
    """
    Dibuja una lista de cuadrados en la pantalla.

    Args:
        lista_cuadrados (list): Lista de diccionarios que representan los cuadrados.

    Returns:
        dict: Último cuadrado dibujado de la lista.
    """
    for cuadrado in lista_cuadrados:
        dibujar_cuadrado(cuadrado)

def dibujar_boton_musical(boton):
    """Descripción: dibuja un boton musical.

    Args:
        boton (): diccionario de donde sacamos los datos.
    """
    boton["ventana"].blit(boton["contenido"], boton["posicion"])

def dibujar_cuadrado(cuadrado:dict):
    """
    Descripción: Dibuja un cuadrado en la ventana.

    Args:
        cuadrado (dict): Diccionario con los datos del cuadrado.
    """
    
    pygame.draw.rect(cuadrado["ventana"], cuadrado["color_actual"], cuadrado["cuadrado"])

def dibujar_texto(texto:dict):
    """Descripción: Muestra solo texto en la ventana.

    Args:
        texto (dict): Diccionario con datos del texto.
    """
    texto["ventana"].blit(texto["texto_escrito"],texto["posicion"])

def dibujar_fondo(pantalla_config:dict,fondo_principal=None):
    """Descripción: Dibuja un fondo de pantalla, dependiendo el parametro opcional, dibujara uno u otro.

    Args:
        pantalla_config (dict): Diccionario donde se obtendran los datos.
        fondo_principal (_type_, optional): parametro opcional que determinara que fondo se dibuja.
    """
    if fondo_principal != None:
        pantalla_config["ventana"].blit(pantalla_config["fondo"],(0,0))
    else:
        pantalla_config["ventana"].blit(pantalla_config["fondo_2"],(0,0))

def dibujar_imagen(imagen:dict):
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

def dibujar_texto_centralizado(input:dict,colores:dict):#!
    """Descripción: Dibuja el texto centralizado dentro de un cuadrado.

    Args:
        input (dict): Diccionario donde se obtendran los datos.
        colores (dict): diccionario de colores
    """
    superficie = renderizar_texto(input["fuente"],input["texto"],colores["negro"],None)#renderizar texto
    input["texto_escrito"] = superficie
    
    rectangulo_texto = superficie.get_rect(center=input["cuadrado"].center)#se obtiene el medio
    input["posicion"] = rectangulo_texto.topleft
    
    dibujar(input,dibujar_cuadrado)#dibujar cuadrado
    
    dibujar(input,dibujar_texto)#blitear pantalla

def dibujar_cartas(carta_1,carta_2):
    """
    Dibuja dos rectángulos que representan cartas.

    Args:
        carta_1 (dict): Diccionario de la primera carta.
        carta_2 (dict): Diccionario de la segunda carta.
    """
    dibujar(carta_1,dibujar_cuadrado)
    dibujar(carta_2,dibujar_cuadrado)

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
