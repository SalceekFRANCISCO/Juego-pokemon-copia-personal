import pygame
from Logica.Log_1_modulo_principal import *

pygame.init() 

elementos_ventana = inicializar_elementos_ventana()

ventana = elementos_ventana[0]
fondo = elementos_ventana[1]
fondo_2 = elementos_ventana[2]

matriz_jerarquias_mezcladas = crear_matriz_jerarquias()

colores = crear_diccionario_colores()

configuracion_pantalla = crear_datos_pantalla(ventana,fondo,fondo_2,colores)

listas = guardar_cartas(configuracion_pantalla,crear_diccionario_listas)
activar_cartas(listas,matriz_jerarquias_mezcladas)

parametros = crear_lista_parametros(2,configuracion_pantalla,listas,colores,matriz_jerarquias_mezcladas)

nuevo_boton_jugar = crear_boton(ventana,("Arial",20),colores,(56,50),(200,60),jugar,parametros[0],"JUGAR")

lista_botones_musicales = crear_lista_botones_musicales(ventana)

elementos_juego = crear_datos_juego(ventana,colores,nuevo_boton_jugar,lista_botones_musicales)

cargar_musica("Musica\Atrapalos Ya!.mp3")

bandera_principal = True

while bandera_principal:

    banderas =  cargar_pantalla_inicial(bandera_principal,configuracion_pantalla,elementos_juego,ventana,colores)

    empezar_juego = banderas[0]
    bandera_principal = banderas[1]
    jugadores = [banderas[2],banderas[3]]
    
    while empezar_juego and bandera_principal:
        juego = manejador_eventos_principal(bandera_principal,empezar_juego,nuevo_boton_jugar, elementos_juego, jugadores, lista_botones_musicales)

        empezar_juego = juego[0]
        bandera_principal = juego[1]

        setear_pantalla(configuracion_pantalla,elementos_juego,jugadores,colores)

        actualizar()

    pygame.quit()