"""
Pygame prosjekt (Fagdag)
Vår 2022 
Areeba N. Chuhan 

sisten-spill
"""


#--------Import packages------------
import pygame
from pygame.locals import *
import sys
import math as math 
from random import choice
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_d, K_a, K_w, K_s)


pygame.init() # initialize pygames 

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


#---------Settings-----------------
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Sisten spill")
keys = pygame.key.get_pressed()

#----------Game variables-----------
system = True 
game_over = False
speedA = 3
speedB = 3 
scoreA = 0
scoreB = 0
tile_size = 30 

#-------------Classes--------------

class Players():
    def __init__(self, color, right, left, up, down):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

        self.image = pygame.Surface([tile_size, tile_size])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, tile_size, tile_size])
        self.rect = self.image.get_rect()
        
    
    def update(self, pixels):
        window.blit(self.image, self.rect)

        dx = 0
        dy = 0 

        keys = pygame.key.get_pressed()
        if keys[self.right]:
            dx += pixels 
        if keys[self.left]:
            dx -= pixels 
        if keys[self.up]:
            dy -= pixels 
        if keys[self.down]:
            dy += pixels
        
        #Check for collision with walls 
        for wall in Walls.wall_list:
            #check for collition in y direction 
            if wall[1].colliderect(self.rect.x, self.rect.y + dy, tile_size, tile_size): 
                #check if below wall
                if keys[self.up]:
                    dy = wall[1].bottom - self.rect.top
                #check if on top of wall
                elif keys[self.down]:
                    dy = wall[1].top - self.rect.bottom
            #check for collition in x direction 
            elif wall[1].colliderect(self.rect.x + dx, self.rect.y, tile_size, tile_size):
                #check if right for wall 
                if keys[self.left]:
                    dx = wall[1].right - self.rect.left
                #check if left for wall
                elif keys[self.right]:
                    dx = wall[1].left - self.rect.right

        #Update player coordinates 
        self.rect.x += dx
        self.rect.y += dy

        #Keep players inside screen 
        if self.rect.right > 630:
            self.rect.right = 630
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 630:
            self.rect.bottom = 630


class Nectar():
    def __init__(self, color):

        self.color = color
    
        self.image = pygame.Surface([tile_size, tile_size])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, tile_size, tile_size])
        self.rect = self.image.get_rect()
        
    def draw(self):
        window.blit(self.image, self.rect)
    
    def changePos(self):
        rand_pos = choice(Walls.nowall_list)
        self.rect.x = rand_pos[0]
        self.rect.y = rand_pos[1]


class Walls():
    def __init__(self, data):
        self.wall_list =  []
        self.nowall_list = []


        #iterate through board data and create all wall-tiles 
        row_count = 0 
        for row in data:
            col_count = 0
            for wall in row:
                if wall == 1: 
                    self.image = pygame.Surface([tile_size,tile_size])
                    self.image.fill(BLACK)
                    self.image.set_colorkey(BLACK)

                    pygame.draw.rect(self.image, BLUE, [0, 0, tile_size, tile_size])
                    rect = self.image.get_rect()
                    rect.x = col_count * tile_size 
                    rect.y = row_count * tile_size
                    wall = (self.image, rect)
                    self.wall_list.append(wall)
                elif wall == 0:
                    position = [col_count*30, row_count*30]
                    self.nowall_list.append(position)
                col_count += 1 
            row_count += 1

    #draw wall-tiles 
    def draw(self):
        for wall in self.wall_list:
            window.blit(wall[0], wall[1])

class Infobox():
    def __init__(self, size, message, ypos):
        self.size = size
        self.message = message
        self.ypos = ypos 
    
    def draw(self):
        font = pygame.font.Font(None, self.size)
        text = font.render(self.message, True, WHITE)
        text_rect = text.get_rect()
        text_x = window.get_width() / 2 - text_rect.width / 2 
        text_y = self.ypos
        text_center = [text_x, text_y]
        window.blit(text, text_center)



#---------Create objects------------
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
]

Walls = Walls(board)

Nectar = Nectar(YELLOW)
Nectar.rect.x = 300
Nectar.rect.y = 300

PlayerA = Players(TURQUOISE, K_d, K_a, K_w, K_s) #har'n
PlayerA.rect.x = 0
PlayerA.rect.y = 0

PlayerB = Players(PURPLE, K_RIGHT, K_LEFT, K_UP, K_DOWN)
PlayerB.rect.x = 600
PlayerB.rect.y = 600
 
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
        


    # 9 - Clear the window
    window.fill(BLACK)


     # 10 - Draw all window elements 
    Nectar.draw()
    Walls.draw()

    # Check for player collition with nectar 
    if Nectar.rect.colliderect(PlayerA.rect):
        Nectar.changePos()
        speedA += 1 
        scoreA += 1
    elif Nectar.rect.colliderect(PlayerB.rect):
        Nectar.changePos()
        speedB += 1
        scoreB += 1
    
    # Check for collition between players 
    if not PlayerA.rect.colliderect(PlayerB.rect):
        PlayerA.update(speedA)
        PlayerB.update(speedB)
    else: 
        Gameover = Infobox(42, "Blue player won!", 250)
        Gameover.draw()


    # Print score in top right corner 
    font = pygame.font.Font(None, 20)
    text = font.render("Blue speed " + str(scoreA), 1, TURQUOISE)
    text2 = font.render("Purple speed " + str(scoreB), 1, PURPLE)
    window.blit(text, (215,10))
    window.blit(text2, (340,10))


    # 11 - Update the window
    pygame.display.flip()
    

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


pygame.quit()