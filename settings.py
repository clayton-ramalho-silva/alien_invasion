"""Uma classe para armazenar todas as configurações da Invasão Alienígena"""
class Settings():   
    
    # Configuraçoes da tela
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #config da espaconave
        self.ship_speed_factor = 1.5
        
        #config projeteis
        self.bullet_speed_facto = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        

