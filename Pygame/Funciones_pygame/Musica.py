import pygame

def cargar_musica(path:str):
    """Descripción:

    Args:
        path (str): _description_
    """
    pygame.mixer.music.load(path)

def reproducir_musica():
    """Descripción:
    """
    pygame.mixer.music.play()

def pausar_musica():
    """Descripción:
    """
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        reanudar_musica()
        
def reanudar_musica():
    """Descripción:
    """
    pygame.mixer.music.unpause()

def detener_musica():
    """Descripción:
    """
    pygame.mixer.music.stop()

def mutear():
    """Descripción:
    """
    pygame.mixer.music.set_volume(0)

def desmutear():
    """Descripción:
    """
    pygame.mixer.music.set_volume(0.3)

def subir_volumen():
    """Descripción:
    """
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual + 0.05)

def bajar_volumen():
    """Descripción:
    """
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual - 0.05)