import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #inicializa o jogo e cria um objeto na tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - by Rodrigo Abreu")

    #Cria uma espaçonave
    ship = Ship(screen)

    # Define uma cor de fundo
    bg_color = (32,124,229,1)

    #inicia o laço principal do jogo
    while True:
        #Observa evento do teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #deixa a tela mais recente visivel
        pygame.display.flip()





run_game()