from turtle import Screen
import sys
import pygame
from ship import Ship

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Play Game - 2022")
    
    #Cria o desenho na tela
    ship = Ship(screen)
    
    #Cores da Tela
    bg_color = (0,191,255)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()

    
run_game()