import pygame
from Logica.Consola_1_MP import *


#NUEVO OBJETIVO: 

#arreglar los modulos de funciones pygame


#MIMIFICAR EL MAIN por ahora bien
#PROBAR CREAR EL MODULO SOLO DICCIONARIOS ya esta hecho
#EMPEZAR CON EL MANEJADOR MUSICAL ya esta hecho
# main mimificado
# PEDIR CORRECTAMENTE LOS NOMBES  



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

clock = pygame.time.Clock()

tiempo_inicial = None
cronometro_activo = False

parametros = crear_listas_parametros(pantalla_config,listas,colores,matriz_jerarquias_mezcladas,cronometro_activo,tiempo_inicial)

nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros[0],"JUGAR")
boton_nombre_uno = crear_boton(ventana,("Arial",20),colores,(1115,27),(175,60),procesar_entrada_texto,parametros[1],"")
boton_nombre_dos = crear_boton(ventana,("Arial",20),colores,(1115,101),(175,60),procesar_entrada_texto,parametros[2],"")

lista_botones_musicales = crear_botones(ventana)

elementos_juego = crear_datos_juego(colores,boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar,lista_botones_musicales)

lista_botones = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

bandera_juego = True
accion_a = None
accion_b = None
acciones = None
#endregion

cargar_musica("Musica\Atrapalos Ya!.mp3")

while bandera_juego: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        # elif evento.type == pygame.MOUSEMOTION:
        #     x,y = evento.pos
        #     print(x,y) #Saber que cordenadas son en la pantalla
        elif evento.type == pygame.KEYDOWN:

            if boton_nombre_uno["activo"]:
                accion_a = detectar_escritura(boton_nombre_uno,evento)

            if boton_nombre_dos["activo"]:
                accion_b = detectar_escritura(boton_nombre_dos,evento)

            acciones = agrupar_acciones(accion_a,accion_b)
                 
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # tiempo_inicial = pygame.time.get_ticks()  
            # cronometro_activo = True 
            jugabilidad(lista_botones,elementos_juego,evento)

            veriificar_accion_botones(lista_botones_musicales, evento)

            

    setear_pantalla(pantalla_config,elementos_juego)

    setear_acciones_pantalla_ses(acciones)

    actualizar()

pygame.quit()