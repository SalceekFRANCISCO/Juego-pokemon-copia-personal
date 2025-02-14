import pygame
from variables import *
from Logica.Consola_1_MP import *

# objetivo: lograr que exitsa un solo boton_jugar en etse caso que sea nuevo_boton_jugar, ver la forma de que los parametros_jugar, los de pantalla puedan guardarse bien

# opcion: crear_2 crear dos diccionarios, uno para datos pantalla, y uno para datos del juego
# el dic pantalla se usa en:
# main principal
# consola 1 2 y 5
# visuales
# dibujo
# y dicc ineraccion







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
def crear_boton(ventana, fuente, colores:tuple, posicion:tuple, dimensiones:tuple,accion,lista_parametros,texto=None) -> dict:
    boton = {}
    boton["ventana"] = ventana
    boton["fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
    boton["color_activo"] = colores["dorado"]
    boton["color_inactivo"] = colores["blanco"]
    boton["activo"] = False
    boton["cuadrado"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
    boton["color_actual"] = colores["blanco"]
    boton["accion"] = accion
    boton["lista_parametros"] = lista_parametros

    if texto != None:
        boton["texto"] = texto

    return boton

def detectar_cambio_color(lista_x,evento):
    for boton in lista_x:
        if boton["cuadrado"].collidepoint(evento.pos):
            cambio_color(boton)

def detectar_jugabilidad(lista_botones,evento):
    for boton in lista_botones:
        if boton["cuadrado"].collidepoint(evento.pos):
            boton["accion"](boton["lista_parametros"])



#endregion


#botones con accion
#region boton_nombre_uno
boton_nombre_uno = crear_input(ventana,fuente,colores,(907,205),(175,60),None,"")
boton_nombre_dos = crear_input(ventana,fuente,colores,(907,362),(175,60),None,"")
#endregion

boton_jugar = crear_input(ventana,fuente,colores,(56,50),(200,60),"JUGAR",None)

lista_x = [boton_nombre_uno,boton_nombre_dos,boton_jugar]

#region
# tiempo_inicial = None
# cronometro_activo = False
# listas = ""
# pantalla = ""

# parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla,colores, cronometro_activo, tiempo_inicial]

# nuevo_boton_jugar = crear_boton(ventana,fuente,colores,(56,50),(200,60),jugar,parametros_jugar,"JUGAR")

# lista_botones = [nuevo_boton_jugar]
#endregion


def crear_datos_pantalla(ventana,color_ventana,lista_cuadrados,pokebola,carta_1,carta_2):
    pantalla_dos = {}
    pantalla_dos["ventana"] = ventana
    pantalla_dos["color_ventana"] = color_ventana
    pantalla_dos["lista_cuadrados"] = lista_cuadrados
    pantalla_dos["pokebola_imagen"] = pokebola
    pantalla_dos["carta_1"] = carta_1
    pantalla_dos["carta_2"] = carta_2

    return pantalla_dos







# region botones con texto
ganador_partida_final = crear_input(ventana,fuente,colores,(1027,60),(200,60),"Ganador partida",None)
atributo = crear_input(ventana,fuente,colores,(1027,439),(200,60),"Atributo Sorteado",None)

pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))

#endregion
#endregion


reemplazo_nombre = False


pantalla = crear_diccionario_pantalla(ventana,GRIS,lista_cuadrados,boton_jugar,reemplazo_nombre,
                                      pokebola,carta_1,carta_2,jugadores,
                                      "Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",
                                      ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos)

listas = guardar_cartas(pantalla,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

#endregion




#region booleanos
clock = pygame.time.Clock()

tiempo_inicial = None
cronometro_activo = False
bandera = True
bandera_dos = False
bandera_tres = False
accion_a = None
accion_b = None
#endregion


parametros_jugar = [5,matriz_jerarquias_mezcladas,listas,pantalla,colores, cronometro_activo, tiempo_inicial]

nuevo_boton_jugar = crear_boton(ventana,fuente,colores,(56,50),(200,60),jugar,parametros_jugar,"JUGAR")

lista_botones = [nuevo_boton_jugar]

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


while bandera: 
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        # elif evento.type == pygame.MOUSEMOTION:
        #     x,y = evento.pos
        #     # print(x,y) #Saber que cordenadas son en la pantalla

        if evento.type == pygame.KEYDOWN:
            if boton_nombre_uno["activo"]:
                texto_pantalla= guardar_texto(pantalla,fuente,colores["negro"],boton_nombre_uno,(795,50),evento,None)
                bandera_dos = True
                accion_a = crear_diccionario_acciones(bandera_dos,texto_pantalla)
           
            if boton_nombre_dos["activo"]:
                texto_pantalla_dos= guardar_texto(pantalla,fuente,colores["negro"],boton_nombre_dos,(797,629),evento,None)
                bandera_tres = True
                accion_b = crear_diccionario_acciones(bandera_tres,texto_pantalla_dos)

                
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # if boton_jugar["cuadrado"].collidepoint(evento.pos): 
                # cambio_color(boton_jugar)
                tiempo_inicial = pygame.time.get_ticks()  
                cronometro_activo = True 

                detectar_cambio_color(lista_x,evento)
                # detectar_cambio_color(lista_botones,evento)
                
                detectar_jugabilidad(lista_botones,evento)
                juego_terminado = True

        elif boton_jugar["activo"]: 
                pantalla["reemplazo_nombre"] = True
                
                if juego_terminado == False:

                    detectar_jugabilidad(lista_botones,evento)
                    juego_terminado = True


    setear_pantalla(pantalla,colores)
    
    setear_acciones_pantalla(accion_a,accion_b)

    actualizar()

pygame.quit()