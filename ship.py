import pygame

class Ship():

    # Inicializa a espaçonave e define sua posição inicial
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaconave
        self.center = float(self.rect.centerx)

        #flag movimento
        self.moving_right = False
        self.moving_left = False
    
    # Atualiza posição da espaconave de acordo com a flag de movimento
    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx += 1
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -= 1

        self.rect.centerx = self.center


    # Desenha a espaçonave na sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)