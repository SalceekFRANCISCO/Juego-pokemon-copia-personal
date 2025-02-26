import pygame
from Logica.Consola_1_MP import *

#OBJETIVOS: 
# Pedir los nombres en la pre-pantalla #!ME FALTA ESTO!
# arreglar el tema del tiempo #!OK
# implementar cartas meza #!OK
# ajustar la velocidad del juego #!OK

# utilizar sets
# mejorar el dry
# utilizar eventos propios
# Mimificar el main  #! va queriendo
# acomodar los modulos Funciones_pygame

# si tengo tiempo y ganas, implementar el submenu musical
# si tengo tiempo y ganas, implementar diccionarios de donde sacar datos

# pedirle a ochoa que me de una devolucion del juego

pygame.init() 
#region
ventana = inicializar_ventana()

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()

# jugadores = identificar_usuarios(2)
jugadores = ["pepe","roberto"]

diccionarios = creacion_diccionarios()

colores = diccionarios[1]

pantalla_config = crear_datos_pantalla(ventana,jugadores)

listas = guardar_cartas(pantalla_config,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

parametros = crear_listas_parametros(pantalla_config,listas,colores,matriz_jerarquias_mezcladas)

nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros[0],"JUGAR")
boton_nombre_uno = crear_boton(ventana,("Arial",20),colores,(1115,27),(175,60),procesar_entrada_texto,parametros[1],"")
boton_nombre_dos = crear_boton(ventana,("Arial",20),colores,(1115,101),(175,60),procesar_entrada_texto,parametros[2],"")

lista_botones_musicales = crear_botones(ventana)

elementos_juego = crear_datos_juego(colores,boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar,lista_botones_musicales)

lista_botones = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

accion_a = None
accion_b = None
acciones = None
#endregion

cargar_musica("Musica\Atrapalos Ya!.mp3")

bandera_principal = True

while bandera_principal:

    banderas =  pantalla_inicial(bandera_principal,pantalla_config,elementos_juego,ventana,colores,parametros)

    empezar_juego = banderas[0]
    bandera_principal = banderas[1]

    while empezar_juego: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_principal = False
                empezar_juego = False
            # region coordenadas
            # elif evento.type == pygame.MOUSEMOTION:
            #     x,y = evento.pos
            #     print(x,y) #Saber que cordenadas son en la pantalla
            #endregion
            
            elif evento.type == pygame.KEYDOWN:
                if boton_nombre_uno["activo"]:
                    accion_a = detectar_escritura(boton_nombre_uno,evento)

                elif boton_nombre_dos["activo"]:
                    accion_b = detectar_escritura(boton_nombre_dos,evento)

                acciones = agrupar_acciones(accion_a,accion_b)
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                detectar_accion(lista_botones,elementos_juego,evento)

                verificar_botones_musicales(lista_botones_musicales, evento)


        setear_pantalla(pantalla_config,elementos_juego)

        setear_acciones_pantalla_ses(acciones)

        actualizar()

pygame.quit()