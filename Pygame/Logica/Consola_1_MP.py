from Funciones_pygame.Dicc_interaccion import *
from Funciones_pygame.Visuales import *
from Logica.Consola_2_FG import *

def cargar_cartas(listas:dict, pantalla:dict, colores:dict): #? ESTA BIEN
    obtener_cartas_cada_jugador(listas) 

    cartas_jugador_1 = listas["cartas_jugadores"][0]
    cartas_jugador_2 = listas["cartas_jugadores"][1]
    ventana = pantalla["ventana"]#! necesitan la ventana
    
    mostrar_cartas(cartas_jugador_1, ventana, colores, (450,0),(150,100),(645,80))#! necesitan la ventana
    mostrar_cartas(cartas_jugador_2, ventana, colores, (450,390),(150,100),(645,500))#! necesitan la ventana

def Determinar_algun_jugador_sin_cartas(listas:list)->bool:
    jugador_sin_cartas = False
    if len(listas["lista_jugador_uno"]) == 0 or len(listas["lista_jugador_dos"]) == 0:  
        jugador_sin_cartas = True
    
    return jugador_sin_cartas

def contar_rondas_jugador(resultado:str,contador_jugador_1:int,contador_jugador_2:int)->list:

    if resultado == "1":
        contador_jugador_1 += 1

    elif resultado == "2":
        contador_jugador_2 += 1

    return [contador_jugador_1,contador_jugador_2]

def cargar_ganador_y_puntaje(pantalla:dict,elementos_pantalla,resultado:str,contador_jugador_1:int,contador_jugador_2:int,colores:dict):

    ganador_ronda = mostrar_ganador_ronda(resultado, pantalla)#! necesita los jugadores
    
    mostrar_texto(elementos_pantalla, ("Arial", 40), ganador_ronda, colores["negro"],(70,450),colores["blanco"])#! muestarn ventana
    
    puntajes = contar_rondas_jugador(resultado,contador_jugador_1,contador_jugador_2)

    mostrar_texto(elementos_pantalla, ("Arial", 50), str(puntajes[0]), colores["negro"], (103, 310),None)#! muestarn ventana
    mostrar_texto(elementos_pantalla, ("Arial", 50), str(puntajes[1]), colores["negro"], (180, 310),None)#! muestarn ventana

    return puntajes

#region
# def jugar(cantidad_rondas, matriz_jerarquias_mezclada,listas, 
#                         pantalla, colores,cronometro_activo,tiempo_inicial):
#     contador = 0
#     contador_jugador_1 = 0
#     contador_jugador_2 = 0

#     while contador < cantidad_rondas or jugador_sin_cartas:
#         jugador_sin_cartas = Determinar_algun_jugador_sin_cartas(listas)
#         contador += 1

#         mostrar_cronometro(pantalla, cronometro_activo,tiempo_inicial,colores)

#         cargar_cartas(listas,pantalla,colores)
        
#         atributo = sortear_atributos(listas["lista_cartas"])
#         mostrar_texto(pantalla, ("Arial", 50),atributo,colores["negro"], (1024,539),None)

#         resultado = comparar_atributos(listas, matriz_jerarquias_mezclada,atributo)
#         agregar_cartas(resultado,listas)

#         puntuacion = cargar_ganador_y_puntaje(pantalla,resultado,contador_jugador_1,contador_jugador_2,colores)
#         contador_jugador_1 = puntuacion[0]
#         contador_jugador_2 = puntuacion[1]

#         actualizar()

#         setear_pantalla(pantalla,colores)

#         pygame.time.delay(1000)

#     ganador_partida = determinar_ganador_partida(pantalla,listas)
#     mostrar_texto(pantalla, ("Arial", 50),ganador_partida,colores["negro"], (1063,139),None)
#     actualizar()

#     puntaje = calcular_puntaje(listas,pantalla, ganador_partida)
#     guardar_resultados(pantalla, puntaje, ganador_partida)


# parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla,colores, cronometro_activo, tiempo_inicial]
#endregion

def jugar(parametros):
    
    cantidad_rondas = parametros[0]
    matriz_jerarquias_mezclada = parametros[1]
    listas = parametros[2]
    pantalla_config = parametros[3]
    elementos_juego = parametros[4]
    colores = parametros[5]
    cronometro_activo = parametros[6]
    tiempo_inicial = parametros[7]

# def jugar(cantidad_rondas, matriz_jerarquias_mezclada,listas, 
#                         pantalla, colores,cronometro_activo,tiempo_inicial):
    contador = 0
    contador_jugador_1 = 0
    contador_jugador_2 = 0

    while contador < cantidad_rondas or jugador_sin_cartas:
        jugador_sin_cartas = Determinar_algun_jugador_sin_cartas(listas)
        contador += 1

        mostrar_cronometro(pantalla_config, cronometro_activo,tiempo_inicial,colores)#! usa la ventana

        cargar_cartas(listas,pantalla_config,colores)#!usa la ventana
        
        atributo = sortear_atributos(listas["lista_cartas"])
        mostrar_texto(pantalla_config, ("Arial", 50),atributo,colores["negro"], (1024,539),None)#!usa la ventana

        resultado = comparar_atributos(listas, matriz_jerarquias_mezclada,atributo)
        agregar_cartas(resultado,listas)

        puntuacion = cargar_ganador_y_puntaje(elementos_juego,pantalla_config,resultado,contador_jugador_1,contador_jugador_2,colores)#! usa los jugadores, otro diccionario
        contador_jugador_1 = puntuacion[0]
        contador_jugador_2 = puntuacion[1]

        actualizar()

        setear_pantalla(pantalla_config,elementos_juego,colores)#!

        pygame.time.delay(1000)

    ganador_partida = determinar_ganador_partida(elementos_juego,listas)#! usa los jugadores, otro diccionario
    mostrar_texto(pantalla_config, ("Arial", 50),ganador_partida,colores["negro"], (1063,139),None)
    actualizar()

    puntaje = calcular_puntaje(listas,elementos_juego, ganador_partida)#! usa los jugadores, otro diccionario
    guardar_resultados(pantalla_config, puntaje, ganador_partida)#! usa el path json, el dicc principal
