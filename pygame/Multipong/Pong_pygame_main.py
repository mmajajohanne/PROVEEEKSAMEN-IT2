""" 
Pygame prosjekt (eksamenstrening) 
Høst 2022 
Areeba N. Chuhan 

Pong-spill
"""


#--------Import packages------------
import pygame
from pygame.locals import *
import sys
import Pong_pygame_classes as Cl
import math as math 
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE)

pygame.init() # initialize pygames 

#---------Define constants----------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255) 
GREEN = (0, 255, 0) 
SIZE = (500, 650)
FRAMES_PER_SECOND = 60


#---------Settings-----------------
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
#icon = pygame.image.load('./Media/black_heart.png')
#pygame.display.set_icon(icon)
pygame.display.set_caption("Pong Game")
#pygame.image.load('./Media/Gyahedi.PNG')
keys = pygame.key.get_pressed()

#---------Create objects------------
mainPad = Cl.Paddle(WHITE, 100, 10)
mainPad.rect.x = 200
mainPad.rect.y = 550

firstBall = Cl.Ball(TURQUOISE, 10, 10)
firstBall.rect.x = 200
firstBall.rect.y = 100

all_balls_sprite = pygame.sprite.Group()
paddle_sprite = pygame.sprite.GroupSingle()
paddle_sprite.add(mainPad)
all_balls_sprite.add(firstBall)

ADDBALL = pygame.USEREVENT + 1 
pygame.time.set_timer(ADDBALL, 3000)


#----------Game variables-----------
system = True 
game_over = False
score = 0
 

# ----------- Main Program Loop ----------------
while system:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:   
            system = False      
            pygame.quit()  
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                system = False 
                pygame.quit()
                sys.exit()
        elif event.type == ADDBALL:
            if game_over == False:
                all_balls_sprite.add(Cl.Ball(TURQUOISE, 10, 10))
    
    mainPad.update(5)
    for x in all_balls_sprite:
        #x.update()
        if x.update() == True:
            pygame.sprite.Group.empty(all_balls_sprite)
            game_over = True
            
        
    #Counts points when collition between paddle and ball 
    for x in all_balls_sprite: 
        if pygame.sprite.collide_mask(x, mainPad):
            x.bounce()
            score += 1

    # 9 - Clear the window
    window.fill(BLACK)
        
    # 10 - Draw all window elements
    all_balls_sprite.draw(window) 
    paddle_sprite.draw(window)

    # Print score in top right corner 
    font = pygame.font.Font(None, 60)
    text = font.render(str(score), 1, WHITE)
    window.blit(text, (450,25))

    if game_over == True:
        Cl.GameOverMSG(42, "Game Over", 300)
        Cl.GameOverMSG(28, f"score: {score}", 350)


    # 11 - Update the window
    pygame.display.flip()
    

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


pygame.quit()
