import pygame
from variables import *
from Logica.Consola_1_MP import *
# from Funciones_pygame.Visuales import *
# from Funciones_pygame.Dicc_interaccion import *

# actualizacion
#borre el return cuadrado de visuales 
#en  dibuajr texto usamos   dibujar_cuadrados(input)
#La funcion dibujar(input) no es necesaria, ni se usa
#La funcion dibujar(rectangulo) no es necesaria, ni se usa
# mostrar texto se modifico
# se modifico casi completo mostrar texto
# ya no se sortea la pokefoto
# hay textbox en pantalla

pygame.init() 

#region A

matriz_jerarquias_mezclada = [["Agua", ("Fuego", "Tierra")],
                    [("Electricidad", "Fuego"),"Tierra"],
                    ["Aire",("Tierra","Agua")],
                    [("Aire", "Hielo"),"Fuego"],
                    ["Electricidad",("Agua", "Hielo")], 
                    [("Normal", "Fuego"),"Psíquico"],
                    ["Normal",("Agua", "Aire")],
                    [("Tierra", "Aire"),"Hielo"]]

ventana = inicializar_ventana()

fuente = ("Arial",20)

# jugadores = identificar_usuarios(2)
jugadores = ["pepe","roberto"]

colores = crear_colores(NEGRO,ROJO,AZUL,AZUL_CLARO,VERDE,BLANCO,DORADO,GRIS)
boton_jugar = crear_input(ventana,fuente,colores,(56,50),(200,60),"JUGAR",None)

ganador_partida_final = crear_input(ventana,fuente,colores,(1027,60),(200,60),"Ganador partida",None)

atributo = crear_input(ventana,fuente,colores,(1027,439),(200,60),"Atributo Sorteado",None)


boton_nombre_uno = crear_input(ventana,fuente,colores,(907,205),(175,60),None,"")

boton_nombre_dos = crear_input(ventana,fuente,colores,(907,362),(175,60),None,"")

boton_reinicio = crear_input(ventana,fuente,colores,(56,50),(200,60),"REINICIO",None)
pokebola = crear_diccionario_imagen(ventana,"Poke_fotos\pokebola.png",(370,145),(530,425))

reemplazo_boton = False

pantalla = crear_diccionario_pantalla(ventana,GRIS,lista_cuadrados,boton_jugar,reemplazo_boton,
                                      boton_reinicio,pokebola,carta_1,carta_2,jugadores,
                                      "Resultados.json","Archivos\Pokemon_Cards_Pygame.csv",
                                      ganador_partida_final,atributo,boton_nombre_uno,boton_nombre_dos)

listas = crear_diccionario_listas()
listas["lista_cartas"] = obtener_datos(pantalla)

mezclar_mazo_cartas(listas)
repartir_cartas(listas)
ordenar_matriz(matriz_jerarquias_mezclada)

clock = pygame.time.Clock()

tiempo_inicial = None
cronometro_activo = False

bandera = True
bandera_dos = False
bandera_tres = False
accion_a = None
accion_b = None

# musica = reproducir_musica("Atrapalos Ya!.mp3", -1, 0.1)

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

# def sexo (pantalla,fuente,colores,boton_nombre_dos,(797,629),evento,texto_fondo):

#     texto_pantalla_dos= guardar_texto(pantalla,fuente,colores["negro"],boton_nombre_dos,(797,629),evento,texto_fondo)
#     bandera_tres = True
#     accion_b = crear_diccionario_acciones(bandera_tres,texto_pantalla_dos)
    
#     return accion_b

def crear_diccionario_acciones(bandera,texto_pantalla):
        accion = {}
        accion["bandera"] = bandera
        accion["texto_pantalla"] = texto_pantalla

        return accion

def setear_accion_pantalla(accion):
    if accion != None:
        if accion["bandera"]:
            dibujar_solo_texto(accion["texto_pantalla"])

def setear_acciones_pantalla(accion_a,accion_b):
        setear_accion_pantalla(accion_a)

        setear_accion_pantalla(accion_b)

juego_terminado = False
while bandera: 
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.MOUSEMOTION:
            x,y = evento.pos
            # print(x,y) #Saber que cordenadas son en la pantalla

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar["cuadrado"].collidepoint(evento.pos): 
                cambio_color(boton_jugar)
                tiempo_inicial = pygame.time.get_ticks()  
                cronometro_activo = True 

            if boton_nombre_uno["cuadrado"].collidepoint(evento.pos):
                cambio_color(boton_nombre_uno)

            if boton_nombre_dos["cuadrado"].collidepoint(evento.pos):
                cambio_color(boton_nombre_dos)

            if boton_reinicio["cuadrado"].collidepoint(evento.pos): 
                cambio_color(boton_reinicio)
                
                nueva_version_jugar(5, matriz_jerarquias_mezclada, listas, pantalla, 
                                        colores, cronometro_activo, tiempo_inicial)
                juego_terminado = True

        elif boton_jugar["activo"]: 
                pantalla["reemplazo_boton"] = True
                
                if juego_terminado == False:

                    nueva_version_jugar(5, matriz_jerarquias_mezclada, listas, pantalla, 
                                        colores, cronometro_activo, tiempo_inicial)
                    juego_terminado = True

        elif evento.type == pygame.KEYDOWN:
            if boton_nombre_uno["activo"]:
                texto_pantalla= guardar_texto(pantalla,fuente,colores["negro"],boton_nombre_uno,(795,50),evento,None)
                bandera_dos = True
                accion_a = crear_diccionario_acciones(bandera_dos,texto_pantalla)
           
            if boton_nombre_dos["activo"]:
                texto_pantalla_dos= guardar_texto(pantalla,fuente,colores["negro"],boton_nombre_dos,(797,629),evento,None)
                bandera_tres = True
                accion_b = crear_diccionario_acciones(bandera_tres,texto_pantalla_dos)


    setear_pantalla(pantalla,colores)

    setear_acciones_pantalla(accion_a,accion_b)

    actualizar()

pygame.quit()