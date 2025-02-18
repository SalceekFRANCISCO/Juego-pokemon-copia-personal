import pygame
from Logica.Consola_1_MP import *

pygame.init() 

ventana = inicializar_ventana()

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()

fuente = ("Arial",20)

# jugadores = identificar_usuarios(2)
jugadores = ["pepe","roberto"]

diccionarios = creacion_diccionarios()

lista_cuadrados = diccionarios[0]
colores = diccionarios[1]

carta_1 = crear_cuadrados(ventana,colores["azul_claro"],(450,26),(340,245))
carta_2 = crear_cuadrados(ventana,colores["rojo"],(450,415),(340,245))

# region botones con texto
ganador_partida_final = crear_input(ventana,fuente,colores,(1027,60),(200,60),"Ganador partida",None)
atributo = crear_input(ventana,fuente,colores,(1027,439),(200,60),"Atributo Sorteado",None)

pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))

#endregion

pantalla_config = crear_datos_pantalla(ventana,colores,lista_cuadrados,pokebola,carta_1,carta_2,"Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",jugadores)

listas = guardar_cartas(pantalla_config,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

clock = pygame.time.Clock()

tiempo_inicial = None
cronometro_activo = False
bandera_juego = True

parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla_config,colores,cronometro_activo,tiempo_inicial]
parametros_nombre = [pantalla_config,fuente,colores["negro"],(795,50),None]
parametros_nombre_dos = [pantalla_config,fuente,colores["negro"],(797,629),None]

nuevo_boton_jugar = crear_boton(ventana,fuente,colores,(56,50),(200,60),jugar,parametros_jugar,"JUGAR")
boton_nombre_uno = crear_boton(ventana,fuente,colores,(907,205),(175,60),procesar_entrada_texto,parametros_nombre,"")
boton_nombre_dos = crear_boton(ventana,fuente,colores,(907,362),(175,60),procesar_entrada_texto,parametros_nombre_dos,"")

elementos_juego = crear_datos_juego(ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar)

lista_botones = [nuevo_boton_jugar]

# lista_botones_nombre = [boton_nombre_uno,boton_nombre_dos]

lista_botones_completa = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

juego_terminado = False
accion_a = None
accion_b = None

while bandera_juego: 
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera_juego = False
        # elif evento.type == pygame.MOUSEMOTION:
        #     x,y = evento.pos
        #     # print(x,y) #Saber que cordenadas son en la pantalla

        if evento.type == pygame.KEYDOWN:
            if boton_nombre_uno["activo"]:
                accion_a = detectar_escritura_individual(boton_nombre_uno,evento)

            elif boton_nombre_dos["activo"]:
                accion_b = detectar_escritura_individual(boton_nombre_dos,evento)

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            tiempo_inicial = pygame.time.get_ticks()  
            cronometro_activo = True 

            detectar_cambio_color(lista_botones_completa,evento)
            
            detectar_jugabilidad(lista_botones,evento,elementos_juego)

            detectar_cambio_nombre(lista_botones)
                
    setear_pantalla(pantalla_config,elementos_juego,colores)

    dibujar(nuevo_boton_jugar,dibujar_cuadrado_con_texto)
    
    setear_acciones_pantalla(accion_a,accion_b)

    actualizar()

pygame.quit()