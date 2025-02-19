import pygame
from Logica.Consola_1_MP import *


#NUEVO OBJETIVO: 
#MIMIFICAR EL MAIN
#PROBAR CREAR EL MODULO SOLO DICCIONARIOS
#EMPEZAR CON EL MANEJADOR MUSICAL
# PEDIR CORRECTAMENTE LOS NOMBES  



pygame.init() 

ventana = inicializar_ventana()

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()

# jugadores = identificar_usuarios(2)
jugadores = ["pepe","roberto"]

diccionarios = creacion_diccionarios()

lista_cuadrados = diccionarios[0]
colores = diccionarios[1]

# region botones con texto
ganador_partida_final = crear_input(ventana,("Arial",20),colores,(1027,60),(200,60),"Ganador partida",None)
atributo = crear_input(ventana,("Arial",20),colores,(1027,439),(200,60),"Atributo Sorteado",None)

#endregion
pantalla_config = crear_datos_pantalla(ventana,colores,lista_cuadrados,jugadores)

listas = guardar_cartas(pantalla_config,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

clock = pygame.time.Clock()

tiempo_inicial = None
cronometro_activo = False

#region #TODO Esto puede ir en una funcion que retorne los parametros
parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla_config,colores,cronometro_activo,tiempo_inicial]
parametros_nombre = [pantalla_config,("Arial",20),colores["negro"],(795,50),None]
parametros_nombre_dos = [pantalla_config,("Arial",20),colores["negro"],(797,629),None]

#endregion 

#region #TODO Esto puede ir en una funcion que retorne los botones con jugabilidad
nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros_jugar,"JUGAR")
boton_nombre_uno = crear_boton(ventana,("Arial",20),colores,(907,205),(175,60),procesar_entrada_texto,parametros_nombre,"")
boton_nombre_dos = crear_boton(ventana,("Arial",20),colores,(907,362),(175,60),procesar_entrada_texto,parametros_nombre_dos,"")
#endregion 

elementos_juego = crear_datos_juego(ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar)

lista_botones = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

bandera_juego = True
accion_a = None
accion_b = None
acciones = None

while bandera_juego: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        # elif evento.type == pygame.MOUSEMOTION:
        #     x,y = evento.pos
        #     # print(x,y) #Saber que cordenadas son en la pantalla
        elif evento.type == pygame.KEYDOWN:

            if boton_nombre_uno["activo"]:
                accion_a = detectar_escritura(boton_nombre_uno,evento)

            if boton_nombre_dos["activo"]:
                accion_b = detectar_escritura(boton_nombre_dos,evento)

            acciones = agrupar_acciones(accion_a,accion_b)
                 
        elif evento.type == pygame.MOUSEBUTTONDOWN:
                tiempo_inicial = pygame.time.get_ticks()  
                cronometro_activo = True 

                detectar_cambio_color(lista_botones,evento)
                
                detectar_jugabilidad(nuevo_boton_jugar,evento,elementos_juego)

    setear_pantalla(pantalla_config,elementos_juego,colores)

    # dibujar(nuevo_boton_jugar,dibujar_cuadrado_con_texto)
    
    setear_acciones_pantalla_ses(acciones)

    actualizar()

pygame.quit()