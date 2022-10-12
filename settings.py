class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienigena"""

    def __init__(self):
        """inicia as configurações do Jogo"""
        #Configurações da Tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5