# def inicializar_ventana():
#     ANCHO_VENTANA = 800
#     ALTO_VENTANA = 400

#     pygame.init()
#     pygame.mixer.init()

#     ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    
#     pygame.display.set_caption("GERpotify")
    
#     icono = pygame.image.load(r"IMG\spo.png")
#     pygame.display.set_icon(icono)

#     fondo = pygame.image.load(r"IMG\fondo.png")
#     fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA, ALTO_VENTANA))

#     return ventana_ppal, fondo

import pygame

def inicializar_ventana():
    ANCHO_VENTANA = 1300
    ALTO_VENTANA = 700

    pygame.init()
    pygame.mixer.init()

    ventana = pygame.display.set_mode(ANCHO_VENTANA,ALTO_VENTANA)

    pygame.display.set_caption("Pokemon Cards")

    return ventana