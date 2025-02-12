# def inicializar_ventana():
#   
# def manejador_eventos(lista_botones):
#     flag_run = True
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             flag_run = False
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             checkear_accion_botones(lista_botones, evento)

#     return flag_run
import pygame

#
def manejador_eventos():
    bandera_correr = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_correr = False
        # elif evento.type == pygame.MOUSEMOTION:
        #     x,y = evento.pos
        #     print(x,y) #Saber que cordenadas son en la pantalla
    
    return bandera_correr
#
#
#
#
#
#
#
#
#
#
#
