# DICCIONARIOS IMPORTA A MUSICA
# INTERACCION IMPORTA A DICCIONARIOS
# VISUALES IMPORTA A DIBUJO Y INTERACCION

#region
# #region sexo
# # def manejador_eventos():
# #     bandera_correr = True
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             bandera_correr = False
# #         # elif evento.type == pygame.MOUSEMOTION:
# #         #     x,y = evento.pos
# #         #     print(x,y) #Saber que cordenadas son en la pantalla
    
# #     return bandera_correr



#  # elif evento.type == pygame.MOUSEBUTTONDOWN:
#         #     if boton_jugar["cuadrado"].collidepoint(evento.pos): 
#         #         # cambio_color(boton_jugar)
#         #         tiempo_inicial = pygame.time.get_ticks()  
#         #         cronometro_activo = True 
            
#         #     #region cosas comentadas

#         #     # elif boton_nombre_uno["cuadrado"].collidepoint(evento.pos):
#         #     #     cambio_color(boton_nombre_uno)

#         #     # elif boton_nombre_dos["cuadrado"].collidepoint(evento.pos):
#         #     #     cambio_color(boton_nombre_dos)

#         #     # detectar_cambio_color(nueva_lista_x,evento)


#         #     # if boton_reinicio["cuadrado"].collidepoint(evento.pos): 
#         #     #     cambio_color(boton_reinicio)
                
#         #         # jugar(5, matriz_jerarquias_mezcladas, listas, pantalla, 
#         #         #                         colores, cronometro_activo, tiempo_inicial)




# # def crear_input(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,texto_del_boton=None,texto_escritura=None) -> dict:
# #     """
# #     Crea un diccionario que representa un campo de entrada (input) en Pygame.

# #     Args:
# #         ventana: Superficie de Pygame donde se dibujará el campo de entrada.
# #         fuente (tuple): Tipo y tamaño de fuente a utilizar (nombre, tamaño).
# #         colores (dict): Diccionario con los colores disponibles.
# #         posicion (tuple): Coordenadas (x, y) del campo de entrada.
# #         dimensiones (tuple): Ancho y alto del campo de entrada.
# #         texto_del_boton (str): Texto inicial del campo de entrada.

# #     Returns:
# #         dict: Diccionario con los datos del campo de entrada.
# #     """
# #     input = {}
# #     input["ventana"] = ventana
# #     # input["fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
# #     input["fuente"] = crear_fuente(fuente[0],fuente[1])
# #     input["color_activo"] = colores["dorado"]
# #     input["color_inactivo"] = colores["blanco"]
# #     input["activo"] = False
# #     input["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
# #     input["color_actual"] = colores["blanco"]

# #     if texto_del_boton != None:
# #         input["texto"] = texto_del_boton # la llave tiene que llamarse texto_del_boton

# #     elif texto_escritura != None:
# #         input["texto_escritura"] = texto_escritura

# #     return input

# #region

# # def crear_diccionario_pantalla(ventana, GRIS, lista_cuadrados, boton_jugar, reemplazo_boton, 
# #                                pokebola, carta_1, carta_2, jugadores, 
# #                                path_json, path_csv, boton_ganador_partida,atributo,boton_nombre_uno,boton_nombre_dos) -> dict:
# #     """
# #     Crea un diccionario que almacena los datos principales de la pantalla.

# #     Args:
# #         ventana: Superficie de Pygame donde se dibujarán los elementos.
# #         GRIS: Color de fondo de la ventana.
# #         lista_cuadrados (list): Lista de cuadrados en la pantalla.
# #         boton_jugar: Botón de inicio del juego.
# #         reemplazo_boton: Botón de reemplazo para alguna acción específica.
# #         boton_reinicio: Botón para reiniciar el juego.
# #         pokebola: Imagen o referencia a la pokebola.
# #         carta_1, carta_2: Cartas asociadas a los jugadores.
# #         jugadores (list): Lista de jugadores (jugador 1 y jugador 2).
# #         path_json (str): Ruta al archivo JSON relacionado.
# #         path_csv (str): Ruta al archivo CSV relacionado.

# #     Returns:
# #         dict: Diccionario con los datos de la pantalla.
# #     """
# #     pantalla = {}
# #     pantalla["ventana"] = ventana
# #     pantalla["color_ventana"] = GRIS
# #     pantalla["lista_cuadrados"] = lista_cuadrados
# #     pantalla["boton_jugar"] = boton_jugar
# #     pantalla["reemplazo_nombre"] = reemplazo_boton
# #     # pantalla["boton_reinicio"] = boton_reinicio
# #     pantalla["pokebola"] = pokebola
# #     pantalla["carta_1"] = carta_1
# #     pantalla["carta_2"] = carta_2
# #     pantalla["jugador_1"] = jugadores[0]
# #     pantalla["jugador_2"] = jugadores[1]
# #     pantalla["path_json"] = path_json
# #     pantalla["path_csv"] = path_csv
# #     pantalla["ganador_partida"] = boton_ganador_partida
# #     pantalla["atributo"] = atributo
# #     pantalla["boton_nombre_uno"] = boton_nombre_uno
# #     pantalla["boton_nombre_dos"] = boton_nombre_dos

# #     return pantalla


# # def procesar_entrada_texto (pantalla:dict,fuente:tuple,color_texto:tuple,boton_nombre:dict,posicion_texto: tuple,evento,color_fondo_texto):#!usa la ventana
# # def procesar_entrada_texto (parametros):
# #     pantalla = parametros[0]
# #     fuente = parametros[1]
# #     color_texto = parametros[2]
# #     boton_nombre = parametros[3]
# #     posicion_texto =  parametros[4]
# #     evento =  parametros[5]
# #     color_fondo_texto = parametros[6]


# #     texto_pantalla = ""
# #     nombre_final = escribir_teclado(boton_nombre,evento)

# #     texto_pantalla = generar_texto_renderizado (pantalla,fuente,nombre_final,color_texto,posicion_texto,color_fondo_texto)
            
# #     return texto_pantalla



# # def jugar(parametros,elementos_juego):
    
# #     cantidad_rondas = parametros[0]
# #     matriz_jerarquias_mezclada = parametros[1]
# #     listas = parametros[2]
# #     pantalla_config = parametros[3]
# #     colores = parametros[4]
# #     cronometro_activo = parametros[5]
# #     tiempo_inicial = parametros[6]

# #     contador = 0
# #     contador_jugador_1 = 0
# #     contador_jugador_2 = 0

# #     while contador < cantidad_rondas or jugador_sin_cartas:
# #         jugador_sin_cartas = Determinar_algun_jugador_sin_cartas(listas)
# #         contador += 1

# #         mostrar_cronometro(pantalla_config, cronometro_activo,tiempo_inicial,colores)#! usa la ventana

# #         cargar_cartas(listas,pantalla_config,colores)#!usa la ventana
        
# #         atributo = mostrar_atributo(listas,pantalla_config,colores)

# #         resultado = comparar_atributos(listas, matriz_jerarquias_mezclada,atributo)
# #         agregar_cartas(resultado,listas)

# #         puntuacion = cargar_ganador_y_puntaje(pantalla_config,resultado,contador_jugador_1,contador_jugador_2,colores)#! usa los jugadores, otro diccionario
# #         contador_jugador_1 = puntuacion[0]
# #         contador_jugador_2 = puntuacion[1]

# #         actualizar_datos(pantalla_config,elementos_juego,colores)

# #     ganador_partida = mostrar_ganador_partida(pantalla_config,listas,colores)

# #     guardar_resultados_finales(ganador_partida,listas,pantalla_config)

# #endregion
# #endregion

# import pygame
# from Funciones_pygame.Musica import *

# cargar_musica("Musica\Atrapalos Ya!.mp3")

# # checkear_accion_botones(lista_botones, evento)

# # Esto va en dicci_interaccion
# def crear_boton_musical(ventana, posicion:tuple, dimensiones:tuple,accion,imagen=None) -> dict:
#     boton_musical = {}
#     boton_musical["ventana"] = ventana
#     boton_musical["dimensiones"] = dimensiones
#     boton_musical["posicion"] = posicion
#     boton_musical["accion"] = accion
#     boton_musical["activo"] = False

#     if boton_musical != None:
#         img = pygame.image.load(imagen)
#         boton_musical["contenido"] = pygame.transform.scale(img,boton_musical["dimensiones"])

#     boton_musical["rectangulo"] = boton_musical["contenido"].get_rect()
#     boton_musical["rectangulo"].topleft = boton_musical["posicion"]


#     return boton_musical

# # Esto va en dicci_interaccion
# def crear_botones(ventana):          #dimen   #posicion
#     # boton_play = crear_boton_musical((50,50), (65,220), ventana,reproducir_musica, "Img_musica\play.png")
#     # boton_pause = crear_boton_musical((50,50), (165,220), ventana,pausar_musica, "Img_musica\pause2.png")
#     # boton_stop = crear_boton_musical((50,50), (265,220), ventana,detener_musica, "Img_musica\stop.png")
#     # boton_up = crear_boton_musical((50,50), (365,220), ventana,subir_volumen, "Img_musica\up.png")
#     # boton_down = crear_boton_musical((50,50), (465,220), ventana,bajar_volumen, "Img_musica\down.png")
#     # boton_mute = crear_boton_musical((50,50), (565,220), ventana,mutear, "Img_musica\mute.png")
#     # boton_unmute= crear_boton_musical((50,50), (665,220), ventana,desmutear, "Img_musica\unmute.png")

#     boton_play = crear_boton_musical(ventana,(65,220),(50,50),reproducir_musica,"Img_musica\play.png")
#     boton_pause = crear_boton_musical(ventana,(165,220),(50,50),pausar_musica,"Img_musica\play.png")
#     boton_stop = crear_boton_musical(ventana,(265,220),(50,50),detener_musica,"Img_musica\play.png")
#     boton_up = crear_boton_musical(ventana,(365,220),(50,50),subir_volumen,"Img_musica\play.png")
#     boton_down = crear_boton_musical(ventana,(465,220),(50,50),bajar_volumen,"Img_musica\play.png")
#     boton_mute = crear_boton_musical(ventana,(565,220),(50,50),mutear,"Img_musica\play.png")
#     boton_unmute = crear_boton_musical(ventana,(665,220),(50,50),desmutear,"Img_musica\play.png")

#     lista = [boton_play, boton_pause, boton_stop, boton_up, boton_down, boton_mute, boton_unmute]
    
#     return lista

# # Esto va en dibujar
# def dibujar_boton_musical(boton):
#     boton["ventana"].blit(boton["contenido"], boton["posicion"])

# # Esto va en dibujar
# def dibujar_botones(lista):
#     for boton in lista:
#         dibujar_boton_musical(boton)

# # Esto va en dicci_interaccion
# def checkear_accion_botones(lista_botones, evento):
#     for boton in lista_botones:
#         if boton["rectangulo"].collidepoint(evento.pos):
#             boton["accion"]()


#endregion



# musica = reproducir_musica ("Atrapalos Ya!.mp3", -1, 0.1)

# pantalla_principal = True
# bandera = True


########################################################################################################################################################
# while bandera:
#     bandera_dos = True

#     while pantalla_principal:
#         pantalla_datos = cargar_pantalla_inicio (pantalla, pantalla_principal, bandera_dos, bandera, 
#                                                  "Who-is-that-Pokemon-/pygame\pokemon fotos\\banderas_fotos\\fondo.jpg", (1000, 900), 
#                                                  "JUGAR", 80, (255, 255, 255), (255, 0, 0), boton_jugar)
#         pantalla_principal = pantalla_datos[0]
#         bandera_dos = pantalla_datos[1]
#         bandera = pantalla_datos[2]

#         pygame.display.update ()

########################################################################################################################################################

#     tiempo_inicial = pygame.time.get_ticks()

#     pokemon_random = uso_random(set_generaciones, generaciones["generaciones.json"]) 

#     gen_random = pokemon_random[0]
#     poke_random = pokemon_random[1]

#     ortografia_fija = ortografia
#     dificultad_fija = dificultad

#     texto = ""
#     partidas_jugadas += 1

#     while bandera_dos:
#         pokemon = generar_imagen_dificultad(dificultad_fija, generaciones["generaciones.json"][gen_random][poke_random]["imagen"], generaciones["generaciones.json"][gen_random][poke_random]["imagen oculta"], 0.09, (500,500),)

#         lista_eventos = pygame.event.get() 
#         for event in lista_eventos: #CAPTURADOR DE EVENTOS
#             if event.type == pygame.QUIT:
#                 bandera_dos = False
#                 bandera = False


#############################################################################################################################

# def manejador_eventos_pantalla (pantalla_principal: bool, bandera: bool, flag_run: bool, boton):
#     for evento_pantalla in pygame.event.get ():
#         if evento_pantalla.type == pygame.QUIT:
#             pantalla_principal = False
#             bandera = False
#             flag_run = False

#         if evento_pantalla.type == pygame.MOUSEBUTTONDOWN:
#             if boton.collidepoint(evento_pantalla.pos):
#                 pantalla_principal = False
    
#     return pantalla_principal, bandera, flag_run
#############################################################################################################################

# def cargar_pantalla_inicio (screen: tuple, bandera_1, bandera_2, bandera_3, 
#                             imagen_fondo: str, escala_fondo: tuple, texto: str, 
#                             size: int, color_texto: tuple, color_boton: tuple, boton):
    
#     jugar = cargar_texto ("Arial", size, True, texto, True, color_texto)
    
#     fondo = cargar_imagen_pantalla (imagen_fondo, escala_fondo)
    
#     pantalla_datos = manejador_eventos_pantalla (bandera_1, bandera_2, bandera_3, boton)

#     screen.blit(fondo, (0,0))
#     pygame.draw.rect (screen, color_boton, boton)
#     screen.blit(jugar, (boton.x + 10, boton.y + 7))

#     return pantalla_datos

#############################################################################################################################
import pygame

pantalla_principal = True
bandera = True

ventana = ""
colores = ""

def crear_datos_pre_pantalla(ventana,colores,bandera_1,bandera_2,bandera_3):
    pre_pantalla = {}
    pre_pantalla["ventana"] = ventana
    pre_pantalla["color_ventana"] = colores["rojo"]
    pre_pantalla["bandera_1"] = bandera_1
    pre_pantalla["bandera_2"] = bandera_2
    pre_pantalla["bandera_3"] = bandera_3

    return pre_pantalla

def cargar_pantalla_inicio(datos,boton):
    manejador_eventos_pantalla(datos,boton)

    rellenar_superficie(datos)
    dibujar_cuadro_con_texto(boton)

    return datos



crear_boton = ""
parametros = ""
jugar = ""




# dad

while bandera:
    bandera_dos = True

    datos = crear_datos_pre_pantalla(ventana,colores,pantalla_principal,bandera_dos,bandera)
    nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros[0],"JUGAR")

    while pantalla_principal:
        cargar_pantalla_inicio(datos,nuevo_boton_jugar), 
        
        pantalla_principal = datos["bandera_1"]
        bandera_dos = datos["bandera_2"]
        bandera = datos["bandera_3"]

        pygame.display.update ()

dibujar_cuadro_con_texto = ""
bandera_1 = "" 
bandera_2 = "" 
bandera_3 = "" 
boton = "" 
rellenar_superficie = ""


# def cargar_pantalla_inicio(datos,boton):
#     pantalla_datos = manejador_eventos_pantalla(datos,boton)

#     rellenar_superficie(datos)
#     dibujar_cuadro_con_texto(boton)

#     return pantalla_datos

def manejador_eventos_pantalla (datos,boton):
    for evento in pygame.event.get ():
        if evento.type == pygame.QUIT:
            datos["pantalla_principal"] = False
            datos["bandera"] = False
            datos["bandera_correr"] = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(evento.pos):
                datos["pantalla_principal"] = False