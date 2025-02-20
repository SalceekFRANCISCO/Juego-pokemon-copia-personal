# def inicializar_ventana():
#   
import pygame
def crear_boton_musical(ventana, posicion:tuple, dimensiones:tuple,accion,imagen=None) -> dict:
    boton_musical = {}
    boton_musical["ventana"] = ventana
    boton_musical["dimensiones"] = dimensiones
    boton_musical["posicion"] = posicion
    boton_musical["accion"] = accion
    boton_musical["activo"] = False

    if boton_musical != None:
        img = pygame.image.load(imagen)
        boton_musical["contenido"] = pygame.transform.scale(img,boton_musical["dimensiones"])

    boton_musical["rectangulo"] = boton_musical["contenido"].get_rect()
    boton_musical["rectangulo"].topleft = boton_musical["posicion"]


    return boton_musical


#
# def manejador_eventos():
#     bandera_correr = True
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             bandera_correr = False
#         # elif evento.type == pygame.MOUSEMOTION:
#         #     x,y = evento.pos
#         #     print(x,y) #Saber que cordenadas son en la pantalla
    
#     return bandera_correr
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
