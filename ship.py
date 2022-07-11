import pygame

class Ship():

    # Inicializa a espaçonave e define sua posição inicial
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom


    # Desenha a espaçonave na sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)