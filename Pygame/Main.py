import pygame
from Logica.Consola_1_MP import *


#NUEVO OBJETIVO: 

#objetivo logrado!!!!



# nuevo objetivo, probar poner los jugadores en el dic prinicpal, asi podes pasar al nuevo boton jugar como elemento para setear en pantalla

#region cambios y ocsas que ocupan espacio 
# from Funciones_pygame.Visuales import *
# from Funciones_pygame.Dicc_interaccion import *

# actualizacion


# esto lo probe desde la pc de mi MAMÁ

#! para las funciones que reciben colores me gustaría, que se pase el diccionario y el color puntual
#! para que busque esa clave en ese diccionario



#borre el return cuadrado de visuales 
#en  dibuajr texto usamos   dibujar_cuadrados(input)
#La funcion dibujar(input) no es necesaria, ni se usa
#La funcion dibujar(rectangulo) no es necesaria, ni se usa
# mostrar texto se modifico
# se modifico casi completo mostrar texto
# ya no se sortea la pokefoto
# hay textbox en pantalla

#endregion

#region cosas 
pygame.init() 

ventana = inicializar_ventana()

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()

fuente = ("Arial",20)

# jugadores = identificar_usuarios(2)
jugadores = ["pepe","roberto"]

diccionarios = creacion_diccionarios()

lista_cuadrados = diccionarios[0]
colores = diccionarios[1]

#endregion

#region funciones

# pantalla = crear_diccionario_pantalla(ventana,GRIS,lista_cuadrados,boton_jugar,reemplazo_nombre,
#                                       pokebola,carta_1,carta_2,jugadores,
#                                       "Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",
#                                       ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos)
#endregion

#region boton_nombre_uno
#botones con accion
# boton_nombre_uno = crear_input(ventana,fuente,colores,(907,205),(175,60),None,"")
# boton_nombre_dos = crear_input(ventana,fuente,colores,(907,362),(175,60),None,"")
#endregion


#endregion
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

#endregion



#region booleanos
clock = pygame.time.Clock()

tiempo_inicial = None
cronometro_activo = False
bandera_juego = True
bandera_dos = False
bandera_tres = False
# accion_a = None
# accion_b = None
#endregion


parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla_config,colores,cronometro_activo,tiempo_inicial]

nuevo_boton_jugar = crear_boton(ventana,fuente,colores,(56,50),(200,60),jugar,parametros_jugar,"JUGAR")

# boton_nombre_uno = crear_input(ventana,fuente,colores,(907,205),(175,60),None,"")
# boton_nombre_dos = crear_input(ventana,fuente,colores,(907,362),(175,60),None,"")


parametros_nombre = [pantalla_config,fuente,colores["negro"],(795,50),None]

parametros_nombre_dos = [pantalla_config,fuente,colores["negro"],(797,629),None]




boton_nombre_uno = crear_boton(ventana,fuente,colores,(907,205),(175,60),procesar_entrada_texto,parametros_nombre,"")
boton_nombre_dos = crear_boton(ventana,fuente,colores,(907,362),(175,60),procesar_entrada_texto,parametros_nombre_dos,"")






# lista_x = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

elementos_juego = crear_datos_juego(ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar)




# lista_botones = [nuevo_boton_jugar]

lista_botones_nombre = [boton_nombre_uno,boton_nombre_dos]

lista_botones_completa = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]



#region
# mostrar ganador partida #!OK
# mejorar la organizacion #! va queriendo
# mostrar atributo sorteado  #!OK
# Implementar manejador de eventos #!ver el ejempl ode fabuan tullo
# Implementar submenu para la música #!verel video de german
# Implementar textbox para ingresar nombre y mostrarlo en pantalla #!OK
# Implementar cartas meza que se muestre. #!preguntar a patricio
# Mejorar el puntaje #!OK
# Mejorar el tema de colores
# mostrar correctamente la estetica #!va queriendo

#endregion

juego_terminado = False
# accion_a = None
# accion_b = None
dibujo = False

while bandera_juego: 
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera_juego = False
        # elif evento.type == pygame.MOUSEMOTION:
        #     x,y = evento.pos
        #     # print(x,y) #Saber que cordenadas son en la pantalla

        if evento.type == pygame.KEYDOWN:
            acciones = detectar_jugabilidad_dos(lista_botones_nombre,evento)

            # accion_a = detectar_escritura_individual(boton_nombre_uno,evento)

            # accion_b = detectar_escritura_individual(boton_nombre_dos,evento)

            # acciones = [accion_a,accion_b]
            dibujo = True

            # if boton_nombre_uno["activo"]:
            #     texto_pantalla= procesar_entrada_texto (pantalla_config,fuente,colores["negro"],boton_nombre_uno,(795,50),evento,None)
            #     bandera_dos = True
            #     accion_a = generar_estado_accion(bandera_dos,texto_pantalla)
           
            # if boton_nombre_dos["activo"]:
            #     texto_pantalla_dos= procesar_entrada_texto (pantalla_config,fuente,colores["negro"],boton_nombre_dos,(797,629),evento,None)#!usan la ventana
            #     bandera_tres = True
            #     accion_b = crear_diccionario_acciones(bandera_tres,texto_pantalla_dos)

                # step 1: ccambiar el color del textbox, eso se hace en detectar_cambio_color()   OK

                # step 2: una vez cambiado el color del textbox, es necesario activar el evento KEYDOWN


        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # if boton_jugar["cuadrado"].collidepoint(evento.pos): 
                # cambio_color(boton_jugar)
                tiempo_inicial = pygame.time.get_ticks()  
                cronometro_activo = True 

                # detectar_cambio_color(lista_x,evento)
                detectar_cambio_color(lista_botones_completa,evento)
                
                # detectar_jugabilidad(lista_botones,evento,elementos_juego)
                # # juego_terminado = True

                # detectar_cambio_nombre(lista_botones)
                
                # if juego_terminado == False:

                #     detectar_jugabilidad(lista_botones,evento)
                #     juego_terminado = True


    setear_pantalla(pantalla_config,elementos_juego,colores)#!usa ambos diccionarios

    dibujar(nuevo_boton_jugar,dibujar_cuadrado_con_texto)
    
    if dibujo == True:
        setear_acciones_pantalla(acciones)

    actualizar()

pygame.quit()