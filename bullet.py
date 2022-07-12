import pygame
from pygame.sprite import Sprite

# Classe administra projeteis disparados pela espaconave
class Bullet(Sprite):

    # Cria objeto para projetil n posição atual da espaconava
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Cria retuangulo para projetil (0,0) em seguida define posicao correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena posicao do projetil como um valor decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    #Move projetil para cima na tela
    def update(self):
        #atualiza posicao decimal projetil
        self.y -= self.speed_factor

        #atualiza posicao do rect
        self.rect.y = self.y

    #Desenha o projetil na tela
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    
