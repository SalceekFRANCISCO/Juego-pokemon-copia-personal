from Logica.Consola_3_FE import *

def identificar_usuarios(cantidad_usuarios:int)->list[str]: 
    """Descripción: Permite que se registren usuarios una x cantidad de veces

    Args:
        cantidad_usuarios (int): cantidad de veces que se podran registrar usuarios.

    Returns:
        list[str]: lista con los nombres
    """
    jugadores = []
    for _ in range(cantidad_usuarios):
        usuario = get_string("Ingrese su nombre: ","Reingrese su nombre: ")
        jugadores.append(usuario)
    
    return jugadores

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

def activar_cartas(listas:dict,matriz_jerarquias_mezcladas:list[list]):
    """Descripcion: mezcla, reparte cartas y ordena la matriz de jerarquias

    Args:
        listas (dict): mazos de los jugadores
        matriz_jerarquias_mezcladas (_type_): Matriz de jerarquias
    """
    
    mezclar_mazo_cartas(listas)
    repartir_cartas(listas)
    ordenar_matriz(matriz_jerarquias_mezcladas)

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
        
        # mostrar_elemento_ganador(elemento_ganador)

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

def mostrar_ganador_ronda(resultado: str, pantalla)->str:#!MODIFICADA AHORA RETORNA AL GANADOR 
    """Muestra y retorna el nombre del ganador de cada ronda.

    Args:
        resultado (str): Recibe un string que indica quien es el ganador.
        jugador_1 (str): Nombre del jugador 1
        jugador_2 (str): Nombre del jugador 2
    """

    jugador_ganador = None
    
    if resultado == "1":
        # print(f"GANA: ¡¡{jugador_1}!!")
        jugador_ganador = pantalla["jugador_1"]#!jugadores, otro diccionario

    elif resultado == "2":
        # print(f"GANA: ¡¡{jugador_2}!!")
        jugador_ganador = pantalla["jugador_2"]#!jugadores, otro diccionario

    elif resultado == "Empate":
        # print("¡¡Es un empate!!")
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

    lista_de_atributos = guardar_atributos(lista_cartas)

    indice = random.randint(0,len(lista_de_atributos)-1)
    
    atributo_sorteado = lista_de_atributos[indice]

    return atributo_sorteado

def guardar_atributos(lista_cartas: list[dict]) -> list: 
    """Guarda en una lista las llaves (atributos) del primer elemento de una lista de diccionarios 
    recibida por parametro exeptuando el nombre.

    Args:
        lista_cartas (list[dict]): lista de diccionarios recibida por parametro.

    Returns:
        list: lista con los atributos o claves de los diccionarios
    """
    lista_atributos = []
    diccionario = lista_cartas[0]

    for atributo in diccionario.keys():
        if atributo != "poke-nombre" and atributo != "poke-foto" :
            lista_atributos.append(atributo)

    return lista_atributos

def determinar_ganador_partida(pantalla:dict,listas:dict) -> str:
    """Determina el ganador de la partida comparando la cantidad de cartas que cada jugador posee. 
    El que posea mas cartas, sera el ganador

    Args:
        lista_jugador_uno (list[dict]): Representa el mazo de cartas del jugador 1
        lista_jugador_dos (list[list]): Representa el mazo de cartas del jugador 2
        jugador_1 (str): Nombre del jugador 1
        jugador_2 (str): Nombre del jugador 2

    Returns:
        str: Ganador de la partida o si hubo un empate.
    """
    
    if len(listas["lista_jugador_uno"]) > len(listas["lista_jugador_dos"]):
        ganador = pantalla["jugador_1"]#!jugadores 
        # print(f"El ganador de la partida es: {jugador_1}")


    elif len(listas["lista_jugador_uno"]) < len(listas["lista_jugador_dos"]):
        ganador = pantalla["jugador_2"]#!jugadores 
        # print(f"El ganador de la partida es: {jugador_2}")

    else: 
        ganador = "Empate"
        # print("Hubo un empate")

    return ganador

def calcular_puntaje(listas, pantalla, jugador_ganador):
    
    if jugador_ganador == pantalla["jugador_1"]:#!jugadores 
        puntaje = len(listas["lista_jugador_uno"])
    
    elif jugador_ganador == pantalla["jugador_2"]:#!jugadores 
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

#region sin uso

# def jugar(path_csv: str, path_json, matriz_jerarquias, cantidad_rondas: int):
#     # matriz_jerarquias = leer_csv_matriz(path_jerarquias)

#     lista_jugador_uno = []
#     lista_jugador_dos = []
#     cartas_jugadores = []
#     cartas_meza = []
#     lista_cartas = []

#     jugadores = identificar_usuarios(2)
    
#     jugador_1 = jugadores[0]
#     jugador_2 = jugadores[1]
    
#     lista_cartas = obtener_datos(path_csv)
#     mezclar_mazo_cartas(lista_cartas)
#     repartir_cartas(lista_cartas, lista_jugador_uno, lista_jugador_dos)
    
#     jugador_sin_cartas = False
#     contador = 0


#     while contador < cantidad_rondas or jugador_sin_cartas == True:
#         contador += 1
#         if len(lista_jugador_uno) == 0 or len(lista_jugador_dos) == 0:  
#             jugador_sin_cartas = True


#         obtener_cartas_cada_jugador(lista_jugador_uno, lista_jugador_dos, cartas_jugadores)
#         print(f"RONDA NÚMERO: {contador}")
#         resultado = comparar_atributos(lista_cartas, cartas_jugadores, matriz_jerarquias)
        
#         agregar_cartas(resultado, lista_jugador_uno, lista_jugador_dos, cartas_meza, cartas_jugadores)

#         print("---------------ESTADISTICAS------------------")
        
#         print(f"El Mazo de la mesa tiene: {len(cartas_meza)} cartas.")
#         print(f"Mazo jugador 1: {jugadores[0]} -- {len(lista_jugador_uno)} cartas.")
#         print(f"Mazo jugador 2: {jugadores[1]} -- {len(lista_jugador_dos)} cartas.")
#         mostrar_ganador_ronda(resultado, jugadores[0], jugadores[1])
#         time.sleep(2)
#         print()
        
#     ganador = determinar_ganador_partida(lista_jugador_uno, lista_jugador_dos, jugador_1, jugador_2)
#     puntaje = calcular_puntaje(lista_jugador_uno, lista_jugador_dos, jugador_1, jugador_2, ganador)
#     guardar_resultados(path_json, puntaje, ganador)

#!Version sin prints
# def jugar(path_csv: str, path_json, matriz_jerarquias, cantidad_rondas: int):
#     lista_jugador_uno = []
#     lista_jugador_dos = []
#     cartas_jugadores = []
#     cartas_meza = []
#     lista_cartas = []

#     jugadores = identificar_usuarios(2)
    
#     jugador_1 = jugadores[0]
#     jugador_2 = jugadores[1]
    
#     lista_cartas = obtener_datos(path_csv)
#     mezclar_mazo_cartas(lista_cartas)
#     repartir_cartas(lista_cartas, lista_jugador_uno, lista_jugador_dos)
    
#     jugador_sin_cartas = False
#     contador = 0

#     while contador < cantidad_rondas or jugador_sin_cartas == True:
#         contador += 1
#         if len(lista_jugador_uno) == 0 or len(lista_jugador_dos) == 0:  
#             jugador_sin_cartas = True


#         obtener_cartas_cada_jugador(lista_jugador_uno, lista_jugador_dos, cartas_jugadores)
#         resultado = comparar_atributos(lista_cartas, cartas_jugadores, matriz_jerarquias)
        
#         agregar_cartas(resultado, lista_jugador_uno, lista_jugador_dos, cartas_meza, cartas_jugadores)

      
#         mostrar_ganador_ronda(resultado, jugadores[0], jugadores[1])
#         time.sleep(2)
        
#     ganador = determinar_ganador_partida(lista_jugador_uno, lista_jugador_dos, jugador_1, jugador_2)
#     puntaje = calcular_puntaje(lista_jugador_uno, lista_jugador_dos, jugador_1, jugador_2, ganador)
#     guardar_resultados(path_json, puntaje, ganador)



#endregion