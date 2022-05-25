import sys
import pygame

def run_game():
    #inicializa o jogo e cria um objeto na tela
    pygame.init()
    screen = pygame.display.set_mode((1100, 650))
    pygame.display.set_caption("Alien Invasion - by Rodrigo Abreu")

    # Define uma cor de fundo
    bg_color = (32,124,229,1)

    #inicia o laço principal do jogo
    while True:
        #Observa evento do teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redesenha a tela a cada passagem pelo laço
        screen.fill(bg_color)

        #deixa a tela mais recente visivel
        pygame.display.flip()





run_game()