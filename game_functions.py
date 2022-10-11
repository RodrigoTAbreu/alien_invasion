import sys
import pygame

def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        elif event.type == pygame.KEYDOWN:  #identificando o movimento ou pressionamento da tecla    
            if event.key == pygame.K_RIGHT: #se for identificado como direita acrescenta +1 na posição centerx ou a direita
                #move a espaçonave para a direita
                ship.rect.centerx +=1 #soma mais um na posição atual
            
    

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Deixa a tela mais recente visivel
    pygame.display.flip()
    
    
