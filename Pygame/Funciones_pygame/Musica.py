import pygame

def cargar_musica(path):
    pygame.mixer.music.load(path)

def reproducir_musica():
    pygame.mixer.music.play()

def pausar_musica():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        reanudar_musica()
        
def reanudar_musica():
    pygame.mixer.music.unpause()

def detener_musica():
    pygame.mixer.music.stop()

def mutear():
    pygame.mixer.music.set_volume(0)

def desmutear():
    pygame.mixer.music.set_volume(0.3)

def subir_volumen():
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual + 0.05)

def bajar_volumen():
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual - 0.05)