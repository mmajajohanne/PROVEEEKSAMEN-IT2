import pygame
from sys import exit

pygame.init() #starts pygame run images and sounds you just need to make it start running
screen = pygame.display.set_mode((800,400)) #lager den svarte ruten du skal spille i
pygame.display.set_caption("Runner") #gir vinduet en tittel
clock = pygame.time.Clock() #gives a clock object

test_surface = pygame.Surface((100,200))
test_surface.fill('Red') #gjør surfacen rød , i pygame er y-aksen positiv nedover. Origon ligger i øverste venstre hjørne


while True:
    for event in pygame.event.get(): #gets events
        if event.type == pygame.QUIT: #sjekker om du krysser ut av vinduet
            pygame.quit() #stenger vinduet, unaniciates everytinh 
            exit() #while løkken stoppes.

    screen.blit(test_surface,(200,100)) #her sier vi at den skal ligge i origon (øverste venstre hjørne)
       
    # draw all our elements
    # update everyething
    pygame.display.update() #ikke kjør koden om kun dette er tilstede, da vil du ikke kunne lukke vinduet, no player input
    clock.tick(60) #while løkken må ikke kjøre mer enn 60 frames per second



