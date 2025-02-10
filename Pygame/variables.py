import pygame
from Logica.Consola_1_MP import *

pygame.init()

ventana = inicializar_ventana()

NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
AZUL_CLARO = (0,150,255)
VERDE = (0,255,0)
BLANCO = (255,255,255)
DORADO = (204, 153, 0)
GRIS = (128, 128, 128)
AMARILLO_CLARO = (254,255,145)

cuadrado_rojo = crear_cuadrados(ventana,ROJO,(56,180),(100,215))
cuadrado_azul = crear_cuadrados(ventana,AZUL_CLARO,(162,180),(100,215))
cuadrado_blanco = crear_cuadrados(ventana,BLANCO,(1122,201),(135,170))
cuadrado_negro_arriba = crear_cuadrados(ventana,NEGRO,(385,80),(520,260))
cuadrado_negro_abajo = crear_cuadrados(ventana,NEGRO,(385,360),(520,260))
carta_1 = crear_cuadrados(ventana,AZUL_CLARO,(450,26),(340,245))
carta_2 = crear_cuadrados(ventana,ROJO,(450,415),(340,245))
lista_cuadrados = [cuadrado_rojo,cuadrado_azul,cuadrado_blanco,cuadrado_negro_arriba,cuadrado_negro_abajo]

