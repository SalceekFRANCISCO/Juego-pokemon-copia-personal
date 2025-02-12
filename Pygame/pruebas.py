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
                    
  # elif evento.type == pygame.MOUSEBUTTONDOWN:
        #     if boton_jugar["cuadrado"].collidepoint(evento.pos): 
        #         # cambio_color(boton_jugar)
        #         tiempo_inicial = pygame.time.get_ticks()  
        #         cronometro_activo = True 
            
        #     #region cosas comentadas

        #     # elif boton_nombre_uno["cuadrado"].collidepoint(evento.pos):
        #     #     cambio_color(boton_nombre_uno)

        #     # elif boton_nombre_dos["cuadrado"].collidepoint(evento.pos):
        #     #     cambio_color(boton_nombre_dos)

        #     # detectar_cambio_color(nueva_lista_x,evento)


        #     # if boton_reinicio["cuadrado"].collidepoint(evento.pos): 
        #     #     cambio_color(boton_reinicio)
                
        #         # jugar(5, matriz_jerarquias_mezcladas, listas, pantalla, 
        #         #                         colores, cronometro_activo, tiempo_inicial)
