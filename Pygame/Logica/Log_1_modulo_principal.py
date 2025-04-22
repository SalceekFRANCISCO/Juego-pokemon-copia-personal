import time 
from Funciones_pygame.Visuales import *
from Logica.Log_2_funciones_generales import *

def jugar(parametros:list,elementos_juego:dict,jugadores:list):
    """Descripción: Empieza a funcionar el juego.

    Args:
        parametros (list): Lista con los parametros necesarios para jugar.
        elementos_juego (dict): Elementos que se dibujaran en la pantalla principal.
        jugadores (list): Los nombres de ambos jugadores.
    """

    cantidad_rondas = parametros[0]
    matriz_jerarquias_mezclada = parametros[1]
    listas = parametros[2]
    pantalla_config = parametros[3]
    colores = parametros[4]
    cronometro_activo = True 
    tiempo_inicial = pygame.time.get_ticks()  

    contador = 0
    contador_jugador_1 = 0
    contador_jugador_2 = 0

    while contador < cantidad_rondas or jugador_sin_cartas:
        jugador_sin_cartas = Determinar_algun_jugador_sin_cartas(listas)
        contador += 1

        mostrar_cronometro(pantalla_config, cronometro_activo,tiempo_inicial,colores)#! usa la ventana

        cargar_cartas(listas,pantalla_config,colores)#!usa la ventana
        
        atributo = mostrar_atributo(listas,pantalla_config,colores)

        resultado = comparar_atributos(listas, matriz_jerarquias_mezclada,atributo)
        agregar_cartas(resultado,listas)
        mostrar_cartas_mesa(pantalla_config,colores,resultado,listas)

        puntuacion = cargar_ganador_y_puntaje(jugadores,pantalla_config,resultado,contador_jugador_1,contador_jugador_2,colores)#! usa los jugadores, otro diccionario
        contador_jugador_1 = puntuacion[0]
        contador_jugador_2 = puntuacion[1]

        actualizar_datos(pantalla_config,elementos_juego,jugadores,colores)

    ganador_partida = mostrar_ganador_partida(jugadores,pantalla_config,listas,colores)

    guardar_resultados_finales(jugadores,ganador_partida,listas,pantalla_config)

def mostrar_cartas_mesa(pantalla:dict,colores:dict,resultado:str,listas:dict):
    """Descripción: 

    Args:
        pantalla (dict): diccionario con datos
        colores (dict): diccionario con colores
        resultado (str): el resultado
        listas (dict): diccionario de listas
    """
    mostrar_texto(pantalla,("Arial", 18),"CARTAS MESA:",colores["negro"],(910,156),None)
    cartas_en_la_meza = "0"

    if resultado == "Empate":
        cartas_en_la_meza = len(listas["cartas_meza"])
        cartas_en_la_meza = str(cartas_en_la_meza)

    mostrar_texto(pantalla,("Arial", 30),cartas_en_la_meza,colores["negro"],(961,192),None)

def cargar_cartas(listas:dict, pantalla:dict, colores:dict):
    """Descripción: Obtiene las cartas de ambos jugadores y las muestra en pantalla. 

    Args:
        listas (dict): diccionario con las listas guardadas.
        pantalla (dict): Las configuraciones de la pantalla.
        colores (dict): Diccionario con los colores.
    """
    obtener_cartas_cada_jugador(listas) 

    cartas_jugador_1 = listas["cartas_jugadores"][0]
    cartas_jugador_2 = listas["cartas_jugadores"][1]

    mostrar_cartas(cartas_jugador_1, pantalla, colores, (450,0),(591,0),(150,100),(645,80))
    mostrar_cartas(cartas_jugador_2, pantalla, colores, (450,390),(591,390),(150,100),(645,500))

def Determinar_algun_jugador_sin_cartas(listas:list)->bool:
    """Descripción: Dterminar si algún jugador se quedo sin cartas.

    Args:
        listas (dict): diccionario con las listas guardadas.

    Returns:
        bool: True o False si alguno gano
    """
    jugador_sin_cartas = False
    if len(listas["lista_jugador_uno"]) == 0 or len(listas["lista_jugador_dos"]) == 0:  
        jugador_sin_cartas = True
    
    return jugador_sin_cartas

def contar_rondas_jugador(resultado:str,contador_jugador_1:int,contador_jugador_2:int)->list:
    """Descripción: Cuenta las rondas que cada jugador va ganando.

    Args:
        resultado (str): EL jugador que gano.
        contador_jugador_1 (int): Las rondas del jugador 1.
        contador_jugador_2 (int): Las rondas del jugador 2.


    Returns:
        list: Ambas cantidad de rondas.
    """
    if resultado == "1":
        contador_jugador_1 += 1

    elif resultado == "2":
        contador_jugador_2 += 1

    return [contador_jugador_1,contador_jugador_2]

def cargar_ganador_y_puntaje(jugadores:list,pantalla:dict,resultado:str,contador_jugador_1:int,contador_jugador_2:int,colores:dict)->list:
    """Descripción: determina el ganador de la ronda y calcula su puntaje.

    Args:
        jugadores (list): Los nombres de ambos jugadores.
        pantalla_config (dict): Lasa configuraciones de la pantalla.
        resultado (str): EL jugador que gano.
        contador_jugador_1 (int): Las rondas del jugador 1.
        contador_jugador_2 (int): Las rondas del jugador 2.
        colores (dict): Diccionario con los colores.

    Returns:
        list: Ambos puntajes de los jugadores.
    """
    ganador_ronda = determinar_ganador_ronda(resultado, jugadores)
    
    mostrar_texto(pantalla, ("Arial", 26), ganador_ronda, colores["negro"],(1120,466),colores["rosa"])
    
    puntajes = contar_rondas_jugador(resultado,contador_jugador_1,contador_jugador_2)

    mostrar_texto(pantalla, ("Arial", 50), str(puntajes[0]), colores["negro"], (103, 310),None)
    mostrar_texto(pantalla, ("Arial", 50), str(puntajes[1]), colores["negro"], (180, 310),None)

    return puntajes

def mostrar_atributo(listas:dict,pantalla_config:dict,colores:dict)->str:
    """Descripción: Sortea un atributo y los muestra en pantalla.

    Args:
        listas (dict): diccionario con las listas guardadas.
        pantalla_config (dict): Las configuraciones de la pantalla.
        colores (dict): Diccionario con los colores.

    Returns:
        str: el atributo sorteado.
    """
    atributo = sortear_atributos(listas["lista_cartas"])
    mostrar_texto(pantalla_config, ("Arial",26),atributo,colores["negro"], (1120,378),colores["rosa"])

    return atributo

def mostrar_ganador_partida(jugadores:list,pantalla_config:dict,listas:dict,colores:dict) -> str:
    """Descripción:  Muestra el ganador de la partida por pantalla.

    Args:
        jugadores (list): Los nombres de ambos jugadores.
        pantalla_config (dict): Las configuraciones de la pantalla.
        listas (dict): diccionario con las listas guardadas.
        colores (dict): Diccionario con los colores.

    Returns:
        str: _description_
    """
    ganador_partida = determinar_ganador_partida(jugadores,listas)
    mostrar_texto(pantalla_config, ("Arial", 26),ganador_partida,colores["negro"], (1118,550),colores["rosa"])
    actualizar()
    pygame.time.delay(1000)

    return ganador_partida

def guardar_resultados_finales(jugadores:list,ganador_partida:str,listas:dict,pantalla_config:dict):
    """Descripción:  Calcula el puntaje final y lo guarda en el archivo json.

    Args:
        jugadores (list): Los nombres de ambos jugadores.
        ganador_partida (str): El ganador de la partida.
        listas (dict): diccionario con las listas guardadas.
        pantalla_config (dict): Las configuraciones de la pantalla.
    """

    puntaje = calcular_puntaje(listas ,jugadores, ganador_partida)
    guardar_resultados(pantalla_config, puntaje, ganador_partida)

def actualizar_datos(pantalla_config:dict,elementos_juego:dict,jugadores:list,colores:dict):
    """Descripción: Actualiza los datos que se muestran en la pantalla.

    Args:
        pantalla_config (dict): Lasa configuraciones de la pantalla.
        elementos_juego (dict): Lasa configuraciones de la pantalla.
        jugadores (list): Los nombres de ambos jugadores.
        colores (dict): Diccionario con los colores.
    """
    actualizar()

    setear_pantalla(pantalla_config,elementos_juego,jugadores,colores)

    # pygame.time.delay(1000)
    # clock.tick(1)
    # time.sleep(10) 
    time.sleep(6) 
