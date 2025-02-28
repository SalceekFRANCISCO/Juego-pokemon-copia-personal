import pygame
from Logica.Consola_1_MP import *


#encontrar una forma de validar que el texto que se escribe tenga mas de 3 caracteres
# fijarse de hacerla en procesar entrada texto

#region
#OBJETIVOS CUMPLIDOS: 
# Pedir los nombres en la pre-pantalla #!OK
# arreglar el tema del tiempo #!OK
# implementar cartas meza #!OK
# ajustar la velocidad del juego #!OK
#endregion

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

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()#estaria bueno que venga de un csv yque tambien se ordene 

diccionarios = creacion_diccionarios()

colores = diccionarios[1]

pantalla_config = crear_datos_pantalla(ventana)

listas = guardar_cartas(pantalla_config,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

parametros = crear_listas_parametros(pantalla_config,listas,colores,matriz_jerarquias_mezcladas)

nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros[0],"JUGAR")

lista_botones_musicales = crear_botones(ventana)

elementos_juego = crear_datos_juego(colores,nuevo_boton_jugar,lista_botones_musicales)

cargar_musica("Musica\Atrapalos Ya!.mp3")

bandera_principal = True

while bandera_principal:

    banderas =  pantalla_inicial(bandera_principal,pantalla_config,elementos_juego,ventana,colores,parametros)

    empezar_juego = banderas[0]
    bandera_principal = banderas[1]
    jugadores = [banderas[2],banderas[3]]

    while empezar_juego: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_principal = False
                empezar_juego = False
            # region coordenadas
            # elif evento.type == pygame.MOUSEMOTION:
            #     x,y = evento.pos
            #     print(x,y) #Saber que cordenadas son en la pantalla
            #region antigua funcion
            # elif evento.type == pygame.KEYDOWN:
            #     if boton_nombre_uno["activo"]:
            #         accion_a = detectar_escritura(boton_nombre_uno,evento)

            #     elif boton_nombre_dos["activo"]:
            #         accion_b = detectar_escritura(boton_nombre_dos,evento)

            #     acciones = agrupar_acciones(accion_a,accion_b)
            #endregion
            #endregion
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                detectar_accion(nuevo_boton_jugar,elementos_juego,jugadores,evento)

                verificar_botones_musicales(lista_botones_musicales, evento)


        setear_pantalla(pantalla_config,elementos_juego,jugadores,colores)

        actualizar()

pygame.quit()