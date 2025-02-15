import pygame
from variables import *
from Logica.Consola_1_MP import *

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

colores = crear_colores(NEGRO,ROJO,AZUL,AZUL_CLARO,VERDE,BLANCO,DORADO,GRIS)

#endregion


#region funciones

# pantalla = crear_diccionario_pantalla(ventana,GRIS,lista_cuadrados,boton_jugar,reemplazo_nombre,
#                                       pokebola,carta_1,carta_2,jugadores,
#                                       "Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",
#                                       ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos)
#endregion


#botones con accion
#region boton_nombre_uno
boton_nombre_uno = crear_input(ventana,fuente,colores,(907,205),(175,60),None,"")
boton_nombre_dos = crear_input(ventana,fuente,colores,(907,362),(175,60),None,"")
#endregion

# boton_jugar = crear_input(ventana,fuente,colores,(56,50),(200,60),"JUGAR",None)

# lista_x = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

#endregion


# region botones con texto
ganador_partida_final = crear_input(ventana,fuente,colores,(1027,60),(200,60),"Ganador partida",None)
atributo = crear_input(ventana,fuente,colores,(1027,439),(200,60),"Atributo Sorteado",None)

pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))

#endregion

pantalla_config = crear_datos_pantalla(ventana,GRIS,lista_cuadrados,pokebola,carta_1,carta_2,"Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",jugadores)


# elementos_juego = crear_datos_juego(ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos,boton_jugar)

#endregion



# pantalla = crear_diccionario_pantalla(ventana,GRIS,lista_cuadrados,boton_jugar,reemplazo_nombre,
#                                       pokebola,carta_1,carta_2,jugadores,
#                                       "Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",
#                                       ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos)

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
accion_a = None
accion_b = None
#endregion


parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla_config,colores,cronometro_activo,tiempo_inicial]

nuevo_boton_jugar = crear_boton(ventana,fuente,colores,(56,50),(200,60),jugar,parametros_jugar,"JUGAR")

# boton_nombre_uno = crear_input(ventana,fuente,colores,(907,205),(175,60),None,"")
# boton_nombre_dos = crear_input(ventana,fuente,colores,(907,362),(175,60),None,"")

evento = ""

parametros_nombre = [pantalla_config,fuente,colores["negro"],boton_nombre_uno,(795,50),evento,None]

parametros_nombre_dos = [pantalla_config,fuente,colores["negro"],boton_nombre_dos,(797,629),evento,None]


boton_nombre_uno = crear_boton(ventana,fuente,colores,(907,205),(175,60),guardar_texto,parametros_nombre,"")
boton_nombre_dos = crear_boton(ventana,fuente,colores,(907,362),(175,60),guardar_texto,parametros_nombre_dos,"")






# lista_x = [boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar]

elementos_juego = crear_datos_juego(ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos,nuevo_boton_jugar)




lista_botones = [nuevo_boton_jugar,boton_nombre_uno,boton_nombre_dos]

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
                texto_pantalla= guardar_texto(pantalla_config,fuente,colores["negro"],boton_nombre_uno,(795,50),evento,None)#!usan la ventana
                bandera_dos = True
                accion_a = crear_diccionario_acciones(bandera_dos,texto_pantalla)
           
            if boton_nombre_dos["activo"]:
                texto_pantalla_dos= guardar_texto(pantalla_config,fuente,colores["negro"],boton_nombre_dos,(797,629),evento,None)#!usan la ventana
                bandera_tres = True
                accion_b = crear_diccionario_acciones(bandera_tres,texto_pantalla_dos)

                
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # if boton_jugar["cuadrado"].collidepoint(evento.pos): 
                # cambio_color(boton_jugar)
                tiempo_inicial = pygame.time.get_ticks()  
                cronometro_activo = True 

                # detectar_cambio_color(lista_x,evento)
                detectar_cambio_color(lista_botones,evento)
                
                detectar_jugabilidad(lista_botones,evento,elementos_juego)
                juego_terminado = True

                detectar_cambio_nombre(lista_botones)
                print(nuevo_boton_jugar["texto"])
                
                if juego_terminado == False:

                    detectar_jugabilidad(lista_botones,evento)
                    juego_terminado = True


    setear_pantalla(pantalla_config,elementos_juego,colores)#!usa ambos diccionarios

    dibujar(nuevo_boton_jugar,dibujar_cuadrado_con_texto)
    

    setear_acciones_pantalla(accion_a,accion_b)

    actualizar()

pygame.quit()