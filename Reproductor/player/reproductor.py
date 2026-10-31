import pygame


class Reproductor:

    def __init__(self):
        pygame.mixer.init()
        self.pausado = False

    def reproducir(self, archivo):
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()
        self.pausado = False

    def pausar(self):
        pygame.mixer.music.pause()
        self.pausado = True

    def reanudar(self):
        pygame.mixer.music.unpause()
        self.pausado = False

    def detener(self):
        pygame.mixer.music.stop()
        self.pausado = False

    def reproduciendo(self):
        return pygame.mixer.music.get_busy()

    def esta_pausado(self):
        return self.pausado
