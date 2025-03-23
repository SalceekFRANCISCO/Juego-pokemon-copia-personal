import pygame

def cargar_musica(path: str):
    """
    Descripción: Carga un archivo de música para que pueda ser reproducido.

    Args:
        path (str): La ruta del archivo de música que se desea cargar.
    """
    pygame.mixer.music.load(path)

def reproducir_musica():
    """
    Descripción: Inicia la reproducción de la música que ha sido cargada previamente con la función `cargar_musica`.
    
    """
    pygame.mixer.music.play()

def pausar_musica():
    """
    Descripción: Pausa la música si está en reproducción.

    """
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        reanudar_musica()

def reanudar_musica():
    """
    Descripción: Reanuda la reproducción de la música que ha sido pausada anteriormente.

    """
    pygame.mixer.music.unpause()

def detener_musica():
    """
    Descripción: Detiene completamente la música que está en reproducción.

    """
    pygame.mixer.music.stop()

def mutear():
    """
    Descripción: Mutea la música, es decir, la pone en volumen cero.

    """
    pygame.mixer.music.set_volume(0)

def desmutear():
    """
    Descripción: Desmuta la música.

    """
    pygame.mixer.music.set_volume(0.3)

def subir_volumen():
    """
    Descripción: Aumenta el volumen de la música en un 5% (0.05) respecto al volumen actual.

    """
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(min(actual + 0.05, 1.0)) 

def bajar_volumen():
    """
    Descripción: Disminuye el volumen de la música en un 5% (0.05) respecto al volumen actual.

    """
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(max(actual - 0.05, 0.0))  
