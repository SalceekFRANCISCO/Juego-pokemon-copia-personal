from Logica.Log_3_funciones_especificas import *

def guardar_cartas(pantalla:dict,funcion)->dict:
    """Descripcion: crea un diccionario de listas vacias y en una de ellas carga los datos necesarios 

    Args:
        pantalla (dict): Donde sacamos los datos
        funcion (_type_): la funcion para crear el diccionario de listas

    Returns:
        dict: _description_
    """
    listas = funcion()
    listas["lista_cartas"] = obtener_datos(pantalla)#!path csv
    
    return listas

def activar_cartas(listas:dict):
    """Descripcion: mezcla y reparte cartas.

    Args:
        listas (dict): mazos de los jugadores
    """
    mezclar_mazo_cartas(listas)
    repartir_cartas(listas)

def comparar_atributos(listas:dict,jerarquias: dict,atributo) -> str: 
    """Descripción: Sortea un atributo al azar y dependiendo el atributo sorteado compara o determina que carta fue la ganadora.

    Args:
        lista_cartas (list[dict]): Lista de cartas normalizada
        cartas_jugadores (list): Las ultimas dos cartas de los jugadores
        jerarquias (dict): Diccionario con las jerarquias de poder de cada poke-elemento.

    Returns:
        str: Que jugador fue el ganador, puede ser el jugador 1, 2 o un Empate.
    """

    elemento_1 = listas["cartas_jugadores"][0]["poke-elemento"]
    elemento_2 = listas["cartas_jugadores"][1]["poke-elemento"]
    
    valor_atributo_1 = listas["cartas_jugadores"][0][atributo]      
    valor_atributo_2 = listas["cartas_jugadores"][1][atributo]

    if atributo == "poke-elemento":

        elemento_ganador = comparar_elementos(jerarquias, elemento_1, elemento_2)
        
        resultado = determinar_resultado(elemento_ganador, elemento_1, elemento_2)

    else:
        valor_atributo_1 = listas["cartas_jugadores"][0][atributo]      
        valor_atributo_2 = listas["cartas_jugadores"][1][atributo]

        atributo_ganador = comparar_valores(valor_atributo_1, valor_atributo_2)
        
        resultado = determinar_resultado(atributo_ganador, valor_atributo_1, valor_atributo_2)
        
    return resultado

def determinar_resultado(parametro_ganador: str|int, parametro_1: str|int, parametro_2: str|int) -> str: 
    """Compara un parametro con otros dos parametros para establecer quien es el ganador.

    Args:
        parametro_ganador (str | int): parametro de referencia
        parametro_1 (str | int): primer parametro
        parametro_2 (str | int): segundo parametro

    Returns:
        str: Devuelve 1 para establecer parametro 1 como ganador, 2 para el parametro 2. En caso de no haber
        coincidencias devolvera Empate.
    """
    if parametro_ganador == parametro_1:
        resultado = "1"
    
    elif parametro_ganador == parametro_2:
        resultado = "2"
    
    else:
        resultado = "Empate"

    return resultado

def determinar_ganador_ronda(resultado: str, jugadores)->str:#!MODIFICADA AHORA RETORNA AL GANADOR 
    """Muestra y retorna el nombre del ganador de cada ronda.

    Args:
        resultado (str): Recibe un string que indica quien es el ganador.
        jugador_1 (str): Nombre del jugador 1
        jugador_2 (str): Nombre del jugador 2
    """

    jugador_ganador = None
    
    if resultado == "1":
        jugador_ganador = jugadores[0]#!jugadores, otro diccionario

    elif resultado == "2":
        jugador_ganador = jugadores[1]#!jugadores, otro diccionario

    elif resultado == "Empate":
        jugador_ganador = "Empate"
    
    return jugador_ganador

def comparar_valores(valor_1: int|float, valor_2: int|float) -> str: 
    """Compara dos valores numericos y devuelve el ganador.

    Args:
        valor_1 (int|float): primer valor recibido
        valor_2 (int|float): segundo valor recibido

    Returns:
        str: Devuelve el valor ganador o empate.
    """
    
    if valor_1 > valor_2:
        resultado = valor_1

    elif valor_1 < valor_2:
        resultado = valor_2

    else:
        resultado = "Empate"

    return resultado

def sortear_atributos(lista_cartas: list[dict]) -> str: 
    """Genera un indice aleatorio de esa lista, y despues busca el valor relacionado 
    a ese indice.

    Args:
        lista_atributos (list): lista de atributos recibida por parametro.

    Returns:
        str: atributo aleatorio.
    """

    # lista_de_atributos = guardar_atributos(lista_cartas)
    # lista_de_atributos = guardar_atributos_set(lista_cartas)

    set_atributos = guardar_atributos(lista_cartas)
    lista_de_atributos = list(set_atributos)

    indice = random.randint(0,len(lista_de_atributos)-1)
    
    atributo_sorteado = lista_de_atributos[indice]

    return atributo_sorteado

def guardar_atributos(lista_cartas: list[dict]) -> set: 
    """Guarda en un set las llaves (atributos) del primer elemento de una lista de diccionarios 
    recibida por parametro exceptuando el nombre.

    Args:
        lista_cartas (list[dict]): lista de diccionarios recibida por parametro.

    Returns:
        list: lista con los atributos o claves de los diccionarios
    """
    set_atributos = set()
    diccionario = lista_cartas[0]

    for atributo in diccionario.keys():
        if atributo != "poke-nombre" and atributo != "poke-foto" :
            set_atributos.add(atributo)

    return set_atributos

def determinar_ganador_partida(jugadores:list,listas:dict) -> str:
    """Descripción: Determina el ganador de la partida comparando la cantidad de cartas que cada jugador posee. 
    El que posea mas cartas, sera el ganador

    Args:
       jugadores (list): Los nombres de ambos jugadores.
       listas (dict): diccionario con las listas guardadas.

    Returns:
        str: Ganador de la partida o si hubo un empate.
    """
    if len(listas["lista_jugador_uno"]) > len(listas["lista_jugador_dos"]):
        ganador = jugadores[0]#!jugadores 


    elif len(listas["lista_jugador_uno"]) < len(listas["lista_jugador_dos"]):
        ganador = jugadores[1]#!jugadores 

    else: 
        ganador = "Empate"

    return ganador

def calcular_puntaje(listas, jugadores, jugador_ganador)->int:
    """Descripcion: Calcula el puntaje de cada jugador.

    Args:
        listas (dict): diccionario con las listas guardadas.
        jugadores (list): Los nombres de ambos jugadores.
        jugador_ganador (str): El jugador ganador.

    Returns:
        int: El puntaje del jugador ganador
    """
    
    if jugador_ganador == jugadores[0]:
        puntaje = len(listas["lista_jugador_uno"])
    
    elif jugador_ganador == jugadores[1]:
        puntaje = len(listas["lista_jugador_dos"])
    
    elif jugador_ganador == "Empate":
        puntaje = len(listas["lista_jugador_uno"])
    
    return puntaje

def obtener_datos(pantalla:dict)->list[dict]:    
    """Descripcion: Crear una lista de diccionarios a partir de un archivo csv 
    normalizando cada uno de los datos recibidos.

    Args:
        path (str): Ruta del archivo csv

    Returns:
        list[dict]: Lista de diccionarios en donde cada diccionario representa
        una carta.
    """
    lista_atributos = leer_csv(pantalla["path_csv"])#!path csv

    nueva_lista = []

    for lista in lista_atributos:
        mi_diccionario = {}
        diccionario_pokemon = normalizar_datos(lista, mi_diccionario)
        nueva_lista.append(diccionario_pokemon)
        
    return nueva_lista
