# Generelt opspsett for pygame 

# ---------Import packages -------------
import pygame
from pygame.locals import *
import sys
import math as math 
from random import choice, randint 
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN)


#---------Define constants----------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255) 
PURPLE = (204, 102, 255)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 77)
GREY = (102, 102, 153)
YELLOW = (255, 210, 77)
SIZE = (630, 630)
FRAMES_PER_SECOND = 60


pygame.init() # initialize pygames 


#---------Settings-----------------
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Sisten spill")
keys = pygame.key.get_pressed()


#---------Game variables--------------
system = True 

#---------Classes---------------------

#----------Create Objects-------------

#----------Main Program Loop----------
while system:

    # Check for and handle events 
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
    
    # CLear the window 

    # Draw all window elements 

    # Program functions and methods 

    # Update window 
    pygame.display.flip()

    # Slow things down 
    clock.tick(FRAMES_PER_SECOND) # make pygame wait 


pygame.quit()