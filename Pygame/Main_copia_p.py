import pygame
from Logica.Consola_1_MP import *
#region
#  los conjuntos (set) solo pueden contener elementos inmutables (hashables), como números, cadenas y tuplas

#encontrar una forma de validar que el texto que se escribe tenga mas de 3 caracteres
# fijarse de hacerla en procesar entrada texto

#region OBJETIVOS CUMPLIDOS
# Pedir los nombres en la pre-pantalla #!OK
# arreglar el tema del tiempo #!OK
# implementar cartas meza #!OK
# ajustar la velocidad del juego #!OK
#endregion

# utilizar sets
# utilizar eventos propios #! ME HAGO EL BOLUDO OK 
# mejorar el dry
# poner fondos relacionados con pokemon #! OK
# acomodar los modulos Funciones_pygame #! OK
# Mimificar el main  #! va queriendo

# si tengo tiempo y ganas, implementar el submenu musical
# si tengo tiempo y ganas, implementar diccionarios de donde sacar datos

# pedirle a ochoa que me de una devolucion del juego
#endregion


#!funciones independientes que funionen en general
#!funciones que tengan una funcion clara
#!no repetir código
#!estudiar conceptos


pygame.init() 
#region
ventanas = inicializar_ventana()

ventana = ventanas[0]
fondo = ventanas[1]
fondo_2 = ventanas[2]

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()#estaria bueno que venga de un csv yque tambien se ordene 

colores = crear_diccionario_colores()

configuracion_pantalla = crear_datos_pantalla(ventana,fondo,fondo_2,colores)

listas = guardar_cartas(configuracion_pantalla,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

parametros = crear_listas_parametros(configuracion_pantalla,listas,colores,matriz_jerarquias_mezcladas)

nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros[0],"JUGAR")

lista_botones_musicales = crear_lista_botones_musicales(ventana)

elementos_juego = crear_datos_juego(ventana,colores,nuevo_boton_jugar,lista_botones_musicales)

cargar_musica("Musica\Atrapalos Ya!.mp3")

bandera_principal = True

while bandera_principal:

    banderas =  pantalla_inicial(bandera_principal,configuracion_pantalla,elementos_juego,ventana,colores,parametros)

    empezar_juego = banderas[0]
    bandera_principal = banderas[1]
    jugadores = [banderas[2],banderas[3]]#! posible set
    #! evento propio para que comienze juego

    while empezar_juego: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_principal = False
                empezar_juego = False
            # region coordenadas
            # elif evento.type == pygame.MOUSEMOTION:
            #     x,y = evento.pos
            #     print(x,y) #Saber que cordenadas son en la pantalla
            #endregion
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                detectar_accion(nuevo_boton_jugar,elementos_juego,jugadores,evento)

                verificar_botones_musicales(lista_botones_musicales, evento)

        setear_pantalla(configuracion_pantalla,elementos_juego,jugadores,colores)

        actualizar()

pygame.quit()