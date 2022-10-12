from operator import truediv
import sys
import pygame

def check_keydown_events(event, ship):
    """Responde ao pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """ Responde a solturas das teclas)"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    
    

def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        elif event.type == pygame.KEYDOWN:  #identificando o movimento ou pressionamento da tecla
            check_keydown_events(event, ship)    
            #if event.key == pygame.K_RIGHT: #se for identificado como direita acrescenta +1 na posição centerx ou a direita
                #move a espaçonave para a direita
                #ship.rect.centerx +=1 #soma mais um na posição atual
            #    ship.moving_right = True #altera a situação de moving_right para TRUE
            #elif event.key == pygame.K_LEFT:
            #    ship.moving_left = True
        elif event.type == pygame.KEYUP:
            check_keydown_events(event, ship) 
            #if event.key == pygame.K_RIGHT:
            #    ship.moving_right = False
            #elif event.key == pygame.K_LEFT:
            #    ship.moving_left = False
                
            
    

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Deixa a tela mais recente visivel
    pygame.display.flip()
    
    
