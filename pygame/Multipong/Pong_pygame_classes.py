"""
All CLasses
- Spill
- Ball 
- Paddle 

All Functions 
- finnAvstnnd 
- gameOverMSG
"""

#--------Import packages----------- 
import pygame
from pygame.locals import *
from random import randint
import math as math
from pygame.locals import (K_LEFT, K_RIGHT)

#--------Define constants----------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255) 
GREEN = (0, 255, 0) 
SIZE = (500, 650)
FRAMES_PER_SECOND = 60

#-----------Settings---------------
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
#icon = pygame.image.load('./Media/black_heart.png')
#pygame.display.set_icon(icon)
pygame.display.set_caption("Pong Game")
#game_over = False

#-------------Classes--------------
class spill: 
    def __init__(self, color, width, height, screen):
        self.color = color  
        self.width = width
        self.height = height
        self.screen = screen


class Paddle(pygame.sprite.Sprite): #Where sprite is a base class for visible game objects 
    def __init__(self, color, width, height):
        #Call parent class (Sprite) constructor 
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
    
    def update(self, pixels):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += pixels 
            if self.rect.x > 400:
                self.rect.x = 400
        if keys[pygame.K_LEFT]:
            self.rect.x -= pixels 
            if self.rect.x < 0:
                self.rect.x = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.velocity = [2, randint(1,5)]

    
    def update(self):
        game_over = False
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #Makes the ball change diraction when contact with walls
        if self.rect.x>=490:
            self.velocity[0] = -self.velocity[0]
        elif self.rect.x<=0:
            self.velocity[0] = -self.velocity[0]
        elif self.rect.y<=0:
            self.velocity[1] = -self.velocity[1] 

        #If ball touches lower wall 
        elif self.rect.y>=640:
            game_over = True  
        return game_over
    
    def bounce(self):
        self.velocity[1] = -self.velocity[1]


class Notis(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.color = color 

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()


    def Draw(self):
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])



#------------Functions--------------
def finnAvstand(obj1, obj2):
    xA2 = (obj1.rect.x - obj2.rect.x)**2 
    yA2 = (obj1.rect.y - obj2.rect.y)**2
    avstand = math.sqrt(xA2 + yA2)
    return avstand 

def GameOverMSG(size, message, ypos):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect()
    text_x = window.get_width() / 2 - text_rect.width / 2 
    text_y = ypos
    text_center = [text_x, text_y]
    window.blit(text, text_center)