#region sexo
# def manejador_eventos():
#     bandera_correr = True
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             bandera_correr = False
#         # elif evento.type == pygame.MOUSEMOTION:
#         #     x,y = evento.pos
#         #     print(x,y) #Saber que cordenadas son en la pantalla
    
#     return bandera_correr



 # elif evento.type == pygame.MOUSEBUTTONDOWN:
        #     if boton_jugar["cuadrado"].collidepoint(evento.pos): 
        #         # cambio_color(boton_jugar)
        #         tiempo_inicial = pygame.time.get_ticks()  
        #         cronometro_activo = True 
            
        #     #region cosas comentadas

        #     # elif boton_nombre_uno["cuadrado"].collidepoint(evento.pos):
        #     #     cambio_color(boton_nombre_uno)

        #     # elif boton_nombre_dos["cuadrado"].collidepoint(evento.pos):
        #     #     cambio_color(boton_nombre_dos)

        #     # detectar_cambio_color(nueva_lista_x,evento)


        #     # if boton_reinicio["cuadrado"].collidepoint(evento.pos): 
        #     #     cambio_color(boton_reinicio)
                
        #         # jugar(5, matriz_jerarquias_mezcladas, listas, pantalla, 
        #         #                         colores, cronometro_activo, tiempo_inicial)




# def crear_input(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,texto_del_boton=None,texto_escritura=None) -> dict:
#     """
#     Crea un diccionario que representa un campo de entrada (input) en Pygame.

#     Args:
#         ventana: Superficie de Pygame donde se dibujará el campo de entrada.
#         fuente (tuple): Tipo y tamaño de fuente a utilizar (nombre, tamaño).
#         colores (dict): Diccionario con los colores disponibles.
#         posicion (tuple): Coordenadas (x, y) del campo de entrada.
#         dimensiones (tuple): Ancho y alto del campo de entrada.
#         texto_del_boton (str): Texto inicial del campo de entrada.

#     Returns:
#         dict: Diccionario con los datos del campo de entrada.
#     """
#     input = {}
#     input["ventana"] = ventana
#     # input["fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
#     input["fuente"] = crear_fuente(fuente[0],fuente[1])
#     input["color_activo"] = colores["dorado"]
#     input["color_inactivo"] = colores["blanco"]
#     input["activo"] = False
#     input["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
#     input["color_actual"] = colores["blanco"]

#     if texto_del_boton != None:
#         input["texto"] = texto_del_boton # la llave tiene que llamarse texto_del_boton

#     elif texto_escritura != None:
#         input["texto_escritura"] = texto_escritura

#     return input

#region

# def crear_diccionario_pantalla(ventana, GRIS, lista_cuadrados, boton_jugar, reemplazo_boton, 
#                                pokebola, carta_1, carta_2, jugadores, 
#                                path_json, path_csv, boton_ganador_partida,atributo,boton_nombre_uno,boton_nombre_dos) -> dict:
#     """
#     Crea un diccionario que almacena los datos principales de la pantalla.

#     Args:
#         ventana: Superficie de Pygame donde se dibujarán los elementos.
#         GRIS: Color de fondo de la ventana.
#         lista_cuadrados (list): Lista de cuadrados en la pantalla.
#         boton_jugar: Botón de inicio del juego.
#         reemplazo_boton: Botón de reemplazo para alguna acción específica.
#         boton_reinicio: Botón para reiniciar el juego.
#         pokebola: Imagen o referencia a la pokebola.
#         carta_1, carta_2: Cartas asociadas a los jugadores.
#         jugadores (list): Lista de jugadores (jugador 1 y jugador 2).
#         path_json (str): Ruta al archivo JSON relacionado.
#         path_csv (str): Ruta al archivo CSV relacionado.

#     Returns:
#         dict: Diccionario con los datos de la pantalla.
#     """
#     pantalla = {}
#     pantalla["ventana"] = ventana
#     pantalla["color_ventana"] = GRIS
#     pantalla["lista_cuadrados"] = lista_cuadrados
#     pantalla["boton_jugar"] = boton_jugar
#     pantalla["reemplazo_nombre"] = reemplazo_boton
#     # pantalla["boton_reinicio"] = boton_reinicio
#     pantalla["pokebola"] = pokebola
#     pantalla["carta_1"] = carta_1
#     pantalla["carta_2"] = carta_2
#     pantalla["jugador_1"] = jugadores[0]
#     pantalla["jugador_2"] = jugadores[1]
#     pantalla["path_json"] = path_json
#     pantalla["path_csv"] = path_csv
#     pantalla["ganador_partida"] = boton_ganador_partida
#     pantalla["atributo"] = atributo
#     pantalla["boton_nombre_uno"] = boton_nombre_uno
#     pantalla["boton_nombre_dos"] = boton_nombre_dos

#     return pantalla


# def procesar_entrada_texto (pantalla:dict,fuente:tuple,color_texto:tuple,boton_nombre:dict,posicion_texto: tuple,evento,color_fondo_texto):#!usa la ventana
# def procesar_entrada_texto (parametros):
#     pantalla = parametros[0]
#     fuente = parametros[1]
#     color_texto = parametros[2]
#     boton_nombre = parametros[3]
#     posicion_texto =  parametros[4]
#     evento =  parametros[5]
#     color_fondo_texto = parametros[6]


#     texto_pantalla = ""
#     nombre_final = escribir_teclado(boton_nombre,evento)

#     texto_pantalla = generar_texto_renderizado (pantalla,fuente,nombre_final,color_texto,posicion_texto,color_fondo_texto)
            
#     return texto_pantalla



# def jugar(parametros,elementos_juego):
    
#     cantidad_rondas = parametros[0]
#     matriz_jerarquias_mezclada = parametros[1]
#     listas = parametros[2]
#     pantalla_config = parametros[3]
#     colores = parametros[4]
#     cronometro_activo = parametros[5]
#     tiempo_inicial = parametros[6]

#     contador = 0
#     contador_jugador_1 = 0
#     contador_jugador_2 = 0

#     while contador < cantidad_rondas or jugador_sin_cartas:
#         jugador_sin_cartas = Determinar_algun_jugador_sin_cartas(listas)
#         contador += 1

#         mostrar_cronometro(pantalla_config, cronometro_activo,tiempo_inicial,colores)#! usa la ventana

#         cargar_cartas(listas,pantalla_config,colores)#!usa la ventana
        
#         atributo = mostrar_atributo(listas,pantalla_config,colores)

#         resultado = comparar_atributos(listas, matriz_jerarquias_mezclada,atributo)
#         agregar_cartas(resultado,listas)

#         puntuacion = cargar_ganador_y_puntaje(pantalla_config,resultado,contador_jugador_1,contador_jugador_2,colores)#! usa los jugadores, otro diccionario
#         contador_jugador_1 = puntuacion[0]
#         contador_jugador_2 = puntuacion[1]

#         actualizar_datos(pantalla_config,elementos_juego,colores)

#     ganador_partida = mostrar_ganador_partida(pantalla_config,listas,colores)

#     guardar_resultados_finales(ganador_partida,listas,pantalla_config)

#endregion
#endregion

import pygame
from Funciones_pygame.Musica import *

cargar_musica("Musica\Atrapalos Ya!.mp3")

# checkear_accion_botones(lista_botones, evento)

# Esto va en dicci_interaccion
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

# Esto va en dicci_interaccion
def crear_botones(ventana):          #dimen   #posicion
    # boton_play = crear_boton_musical((50,50), (65,220), ventana,reproducir_musica, "Img_musica\play.png")
    # boton_pause = crear_boton_musical((50,50), (165,220), ventana,pausar_musica, "Img_musica\pause2.png")
    # boton_stop = crear_boton_musical((50,50), (265,220), ventana,detener_musica, "Img_musica\stop.png")
    # boton_up = crear_boton_musical((50,50), (365,220), ventana,subir_volumen, "Img_musica\up.png")
    # boton_down = crear_boton_musical((50,50), (465,220), ventana,bajar_volumen, "Img_musica\down.png")
    # boton_mute = crear_boton_musical((50,50), (565,220), ventana,mutear, "Img_musica\mute.png")
    # boton_unmute= crear_boton_musical((50,50), (665,220), ventana,desmutear, "Img_musica\unmute.png")

    boton_play = crear_boton_musical(ventana,(65,220),(50,50),reproducir_musica,"Img_musica\play.png")
    boton_pause = crear_boton_musical(ventana,(165,220),(50,50),pausar_musica,"Img_musica\play.png")
    boton_stop = crear_boton_musical(ventana,(265,220),(50,50),detener_musica,"Img_musica\play.png")
    boton_up = crear_boton_musical(ventana,(365,220),(50,50),subir_volumen,"Img_musica\play.png")
    boton_down = crear_boton_musical(ventana,(465,220),(50,50),bajar_volumen,"Img_musica\play.png")
    boton_mute = crear_boton_musical(ventana,(565,220),(50,50),mutear,"Img_musica\play.png")
    boton_unmute = crear_boton_musical(ventana,(665,220),(50,50),desmutear,"Img_musica\play.png")

    lista = [boton_play, boton_pause, boton_stop, boton_up, boton_down, boton_mute, boton_unmute]
    
    return lista

# Esto va en dibujar
def dibujar_boton_musical(boton):
    boton["ventana"].blit(boton["contenido"], boton["posicion"])

# Esto va en dibujar
def dibujar_botones(lista):
    for boton in lista:
        dibujar_boton_musical(boton)

# Esto va en dicci_interaccion
def checkear_accion_botones(lista_botones, evento):
    for boton in lista_botones:
        if boton["rectangulo"].collidepoint(evento.pos):
            boton["accion"]()




