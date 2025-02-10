from Logica.Consola_4_IC import *
from Logica.Consola_5_MA import *

def validate_lenght(caracter: str,mensaje_error: str) -> bool:
        while caracter.islower() != True:
            caracter = input(mensaje_error)

        return caracter

def get_string(mensaje: str,mensaje_error: str)->str:
    """Descripción: Valida si el carácter ingresado esta dentro del limite permitido.

    Args:
        longitud (int): El largo permitido.
        mensaje (str): Mensaje para pedir el dato.
        mensaje_error (str): Mensaje de error, vuelve a pedir el dato.

    Returns:
        str: Informa si pudo validar el caracter.
    """
    string_txt = input(mensaje)

    texto = validate_lenght(string_txt,mensaje_error)

    return texto

def obtener_valores_numericos(caracter:str, entero=False)-> int|float:
    """Convierte una cadena numerico a valor entero o flotante.

    Args:
        caracter (str): cadena recibida por parametro
        entero (bool, optional): Si esta en False, convierte a flotante. Si esta en True
        convierte el valor a entero

    Returns:
        int|float: Valor entero o flotante
    """
    caracter = float(caracter)                                             

    if entero:
        caracter = int(caracter) 

    return caracter

def normalizar_datos(lista:list, diccionario:dict)->dict:   
    """Recibe una lista de elementos, normaliza cada valor(atributo). En el diccionario
    que recibe, crea las llaves y guarda sus datos normalizados.

    Args:
        lista (list): Lista de atributos que recibe por parametro
        diccionario (dict): Diccionario que recibe por parametro

    Returns:
        dict: diccionario con los datos normalizados de la lista
    """

    nombre = lista[0]
    diccionario["poke-nombre"] = nombre
    
    velocidad = obtener_valores_numericos(lista[1],True)
    diccionario["poke-velocidad"] = velocidad

    fuerza = obtener_valores_numericos(lista[2],True)
    diccionario["poke-fuerza"] = fuerza

    poke_elemento = lista[3]       
    diccionario["poke-elemento"] = poke_elemento

    peso = obtener_valores_numericos(lista[4])
    diccionario["poke-peso"] = peso

    altura = obtener_valores_numericos(lista[5])
    diccionario["poke-altura"] = altura

    poke_foto = lista[6]
    diccionario["poke-foto"] = poke_foto

    return diccionario

############################### MATRIZ ############################
def buscar_elementos_en_matriz(matriz: list[list], elemento: str, columna = 0) -> list:      
    """Busca un string en la columna especificada (por defecto 0) en una matriz

    Args:
        matriz (list[list]): matriz recibida por parametro
        elemento (str): elemento/cadena a buscar en la matriz
        columna (int, optional): numero de columna de la matriz donde se desea buscar.
    Returns:
        list: Devuelve la lista del elemento encontrado
    """
    lista = []
    for i in range(len(matriz)):
        if elemento == matriz[i][columna]:
            lista = matriz[i]
            break
    
    return lista

def buscar_elementos_en_lista(lista: list, elemento: str) -> bool: 
    """Busca un string en una lista pasada por parametro

    Args:
        lista (list): lista recibida por parametro
        elemento (str): elemento a buscar recibido por parametro

    Returns:
        bool: Devuelve True si lo encontro
    """
    encontrado = False
    for i in range(len(lista)):
        if elemento == lista[i]:
            encontrado = True
    return encontrado

def comparar_elementos(matriz: list[list], elemento_1: str, elemento_2: str) -> str: 
    """Compara dos strings recibidos por parametro. Los evalua siguendo el criterio establecido
    en la matriz y retorna el elemento ganador, si lo hay.

    Args:
        matriz (list[list]): matriz que establece el criterio de comparacion recibida por parametro
        elemento_1 (str): primer elemento recibido por parametro
        elemento_2 (str): segundo elemento recibido por parametro

    Returns:
        str: Devuelve el elemento ganador. Si no hay ganador devuelve Empate
    """

    fila_elemento_1 = buscar_elementos_en_matriz(matriz, elemento_1)
    fila_elemento_2 = buscar_elementos_en_matriz(matriz, elemento_2)

    derrota_elemento_1 = buscar_elementos_en_lista(fila_elemento_2[1], elemento_1)
    derrota_elemento_2 = buscar_elementos_en_lista(fila_elemento_1[1], elemento_2)

    if derrota_elemento_1 == True:
        ganador = elemento_2
    elif derrota_elemento_2 == True:
        ganador = elemento_1
    else:
        ganador = "Empate"
    return ganador

############################### ORDENAMIENTO ############################
def ordenar_matriz(matriz: list[list]):   
    """Ordena una matriz colocando los strigs al principio de la lista y luego las tuplas.

    Args:
        matriz (list[list]): matriz recibida por parametro
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            for k in range(j+1, len(matriz[i])):
                if type(matriz[i][j]) != str and type(matriz[i][k]) == str:
                    auxiliar = matriz[i][j]
                    matriz[i][j] = matriz[i][k]
                    matriz[i][k] = auxiliar