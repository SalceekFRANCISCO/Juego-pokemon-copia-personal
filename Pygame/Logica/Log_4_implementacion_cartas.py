import random

def mezclar_mazo_cartas(listas:list):
    """Mezcla los elementos de una lista en una cantidad random de veces.
    Genera dos valores aleatorios, luego identifica los diccionarios cuyos indices sean
    iguales a los valores aleatorios y luego los intercambia de posicion. 

    Args:
        lista (list): lista recibida por parametro.
    """
    contador = 0
    cantidad_veces_mezclado = random.randint(10, 50) 

    while contador != cantidad_veces_mezclado:

        indice_random_a = random.randint(0,len(listas["lista_cartas"])-1)
        indice_random_b = random.randint(0,len(listas["lista_cartas"])-1)

        diccionario_a = listas["lista_cartas"][indice_random_a]
        diccionario_b = listas["lista_cartas"][indice_random_b]

        listas["lista_cartas"][indice_random_a] = diccionario_b 
        listas["lista_cartas"][indice_random_b] = diccionario_a 

        contador += 1

def obtener_cartas_cada_jugador(listas:list):  
    """Recibe dos listas que representan dos mazos de cartas. Extrae la ultima carta de
    cada mazo y las guarda en una nueva lista (cartas_jugadores). 

    Args:
        listas["lista_jugador_uno"] (list): Representa el mazo de cartas correspondiente al jugador 1
        lista_jugador_dos (list): Representa el mazo de cartas correspondiente al jugador 2
        listas["cartas_jugadores"] (list): Lista donde se guardaran las cartas obtenidas de cada mazo

    """
    if listas["lista_jugador_uno"] and listas["lista_jugador_dos"]: #verifico que la lista no este vacia
        carta_jugador_1 = listas["lista_jugador_uno"].pop()
        carta_jugador_2 = listas["lista_jugador_dos"].pop()

        listas["cartas_jugadores"].append(carta_jugador_1)
        listas["cartas_jugadores"].append(carta_jugador_2)

def agregar_cartas(resultado:str,listas):  #Terminada
    """Descripción: Agrega las cartas de los jugadores y las suma al pilon de la mesa, si gano alguno de los jugadores.
    Las cartas de la mesa se sumaran a su mazo, de lo contrario las cartas permaneceran en la mesa. 

    Args:
        resultado (str): El Jugador que resulto ganador
        lista_jugador_uno (list[dict]): Cartas del primer jugador
        lista_jugador_dos (list[dict]): Cartas del segundo jugador
        cartas_meza (list[dict]): Las cartas de la meza
        cartas_jugadores (list[dict]): Las cartas de los jugadores
    """
    listas["cartas_meza"] += listas["cartas_jugadores"]
    
    if resultado == "1":
        for carta in listas["cartas_meza"]:
            listas["lista_jugador_uno"].insert(0, carta)
        listas["cartas_meza"].clear()

    elif resultado == "2":
        for carta in listas["cartas_meza"]:
            listas["lista_jugador_dos"].insert(0, carta)
        listas["cartas_meza"].clear()
    
    listas["cartas_jugadores"].clear()

def repartir_cartas(listas):
    """Divide la lista de cartas en dos listas iguales.

    Args:
        lista_cartas (list): Lista recibida por parámetro
        lista_jugador_uno (list): Lista recibida por parámetro del primer jugador
        lista_jugador_dos (list): Lista recibida por parámetro del segundo jugador
    """
    
    for i in range(len(listas["lista_cartas"])):
        
        if i % 2 == 0:
            listas["lista_jugador_uno"].append(listas["lista_cartas"][i])

        elif i % 2 != 0:
            listas["lista_jugador_dos"].append(listas["lista_cartas"][i])

#region RECURSIVA

# def repartir_cartas(listas: list[dict], indice=0):
#     """Divide la lista de cartas en dos listas iguales de forma recursiva.

#     Args:
#         listas["lista_cartas"] (list): Lista recibida por parámetro de todas las cartas
#         listas["lista_jugador_uno"] (list): Lista recibida por parámetro del primer jugador
#         ["lista_jugador_dos"] (list): Lista recibida por parámetro del segundo jugador
#         indice (int): Índice de la carta que se está procesando, se inicializa en 0.
#     """
#     if indice < len(listas["lista_cartas"]):  #condicion de corte
#         if indice % 2 == 0:
#             listas["lista_jugador_uno"].append(listas["lista_cartas"][indice])
#         else:
#             listas["lista_jugador_dos"].append(listas["lista_cartas"][indice])
        
#         repartir_cartas(listas, indice + 1)

#endregion 