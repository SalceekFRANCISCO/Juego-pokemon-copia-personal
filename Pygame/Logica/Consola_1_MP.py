from Funciones_pygame.Dicc_interaccion import *
from Funciones_pygame.Visuales import *
from Logica.Consola_2_FG import *

def cargar_cartas(listas:dict, pantalla:dict, colores:dict): #? ESTA BIEN
    obtener_cartas_cada_jugador(listas) 

    cartas_jugador_1 = listas["cartas_jugadores"][0]
    cartas_jugador_2 = listas["cartas_jugadores"][1]
    ventana = pantalla["ventana"]
    
    mostrar_cartas(cartas_jugador_1, ventana, colores, (450,0),(150,100),(645,80))
    mostrar_cartas(cartas_jugador_2, ventana, colores, (450,390),(150,100),(645,500))

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

def cargar_ganador_y_puntaje(pantalla:dict,resultado:str,contador_jugador_1:int,contador_jugador_2:int,colores:dict):

    ganador_ronda = mostrar_ganador_ronda(resultado, pantalla)
    
    mostrar_texto(pantalla, ("Arial", 40), ganador_ronda, colores["negro"],(70,450),colores["blanco"])
    
    puntajes = contar_rondas_jugador(resultado,contador_jugador_1,contador_jugador_2)

    mostrar_texto(pantalla, ("Arial", 50), str(puntajes[0]), colores["negro"], (103, 310),None)
    mostrar_texto(pantalla, ("Arial", 50), str(puntajes[1]), colores["negro"], (180, 310),None)

    return puntajes

def jugar(cantidad_rondas, matriz_jerarquias_mezclada,listas, 
                        pantalla, colores,cronometro_activo,tiempo_inicial):
    contador = 0
    contador_jugador_1 = 0
    contador_jugador_2 = 0

    while contador < cantidad_rondas or jugador_sin_cartas:
        jugador_sin_cartas = Determinar_algun_jugador_sin_cartas(listas)
        contador += 1

        mostrar_cronometro(pantalla, cronometro_activo,tiempo_inicial,colores)

        cargar_cartas(listas,pantalla,colores)
        
        atributo = sortear_atributos(listas["lista_cartas"])
        mostrar_texto(pantalla, ("Arial", 50),atributo,colores["negro"], (1024,539),None)

        resultado = comparar_atributos(listas, matriz_jerarquias_mezclada,atributo)
        agregar_cartas(resultado,listas)

        puntuacion = cargar_ganador_y_puntaje(pantalla,resultado,contador_jugador_1,contador_jugador_2,colores)
        contador_jugador_1 = puntuacion[0]
        contador_jugador_2 = puntuacion[1]

        actualizar()

        setear_pantalla(pantalla,colores)

        pygame.time.delay(1000)

    ganador_partida = determinar_ganador_partida(pantalla,listas)
    mostrar_texto(pantalla, ("Arial", 50),ganador_partida,colores["negro"], (1063,139),None)
    actualizar()
    # print(f"se mostro: {ganador_partida}")
    # pygame.time.delay(1000)
    # setear_pantalla(pantalla,colores)

    puntaje = calcular_puntaje(listas,pantalla, ganador_partida)
    guardar_resultados(pantalla, puntaje, ganador_partida)
