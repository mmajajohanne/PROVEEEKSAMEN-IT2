import pygame
import random
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d)

pygame.init()

vindu_bredde=630
vindu_hoyde=630

rute = 30

skjerm = pygame.display.set_mode((vindu_bredde,vindu_hoyde))
pygame.display.set_caption("Spill")

rutenett_data = [
[],
[],
[2,3,4,5,6,7,8,12,13,14,15,16,17,18],
[],
[],
[5],
[5],
[5],
[5,8,9,10,11,12,15],
[5,15],
[5,15],
[5,15],
[5,8,9,10,11,12,15],
[15],
[15],
[15],
[],
[],
[],
[2,3,4,5,6,7,8,12,13,14,15,16,17,18],
]

vegger = [] #liste med firkantene som skal tegnes, altså at de skal bli vegger
vegger_rektangler = [] #rektanglene til veggene - brukes til kollisjonsdetekjon


class Firkant():
    def __init__(self, vindu,farge,x,y,sidekant):
        self.vindu = vindu
        self.farge = farge
        self.x = x
        self.y = y
        self.sidekant = sidekant
        self.rekt = pygame.Rect(self.x,self.y,self.sidekant,self.sidekant)
        self.last_slowdown_time = pygame.time.get_ticks()

    def tegnFirkant(self):
        pygame.draw.rect(self.vindu, self.farge,(self.x,self.y,self.sidekant,self.sidekant))
        self.rekt = pygame.Rect(self.x,self.y,self.sidekant,self.sidekant)

class Spiller(Firkant):
    def __init__(self, vindu, farge, x, y, sidekant,fart,styretaster):
        super().__init__(vindu, farge, x, y, sidekant)

        self.fart = fart
        self.styretaster = styretaster

    def flytt(self, taster):

        """Metode for å flytte firkanten"""
        ny_x = self.x
        ny_y = self.y
        #kopierer posisjonen

        if taster[self.styretaster[0]]:
            ny_y -= self.fart
            if ny_y <=0:
                ny_y = 0

        if taster[self.styretaster[1]]:
            ny_y += self.fart
            if ny_y >= 600:
                ny_y = 600

        if taster[self.styretaster[2]]:
            ny_x -= self.fart
            if ny_x <= 0:
                ny_x = 0
                
        if taster[self.styretaster[3]]:
            ny_x += self.fart
            if ny_x >= 600:
                ny_x = 600

        if not self.vegg_kollisjonsdeteksjon(ny_x,ny_y):
            self.x = ny_x
            self.y = ny_y

    def kollisjonsdeteksjon(self,motspiller):
        if self.rekt.colliderect(motspiller.rekt):
            self.fart = 0
            motspiller.fart = 0

    def vegg_kollisjonsdeteksjon(self,x,y):
        for vegg in vegger_rektangler:
            if vegg.colliderect(x,y,self.sidekant,self.sidekant):
                return True
            # finne ut om noe kolliderer
            # flytte spiller ut av kollisjonen
        return False
    
    def gradvisFartstap(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_slowdown_time > 1000:  # check if 30 seconds have passed
            self.fart += -0.2  # slow down speed by 0.1
            self.last_slowdown_time = current_time  # record new time
    
    def endreFartEtterNektar(self):
        if self.rekt.colliderect(nektar.rekt):
            self.fart += 0.5

            ny_x = random.randint(0,630)
            ny_y  = random.randint(0,630)

            if not self.vegg_kollisjonsdeteksjon(ny_x,ny_y):
                nektar.x = ny_x
                nektar.y = ny_y


sisten = Spiller(skjerm,(255,0,0),0,0,30,5,[K_UP,K_DOWN,K_LEFT,K_RIGHT])
haren = Spiller(skjerm,(0,0,255),600,600,30,5,[K_w,K_s,K_a,K_d])
nektar = Firkant(skjerm,(255,255,0),300,300,30)


def draw_grid():
    for linje in range (0,21):
        pygame.draw.line(skjerm, (255,255,255), (0,linje*rute),(vindu_bredde,linje*rute))
        pygame.draw.line(skjerm, (255,255,255), (linje*rute,0),(linje*rute,vindu_hoyde))

for i in range (len(rutenett_data)):
    for j in range (len(rutenett_data[i])):
        vegg = Firkant(skjerm,(0,0,0),rutenett_data[i][j]*rute,i*rute,rute)
        vegger.append(vegg)
        vegger_rektangler.append(vegg.rekt)

kjor = True
clock = pygame.time.Clock()

while kjor:
    
    skjerm.fill((0,200,255))
    
    trykkede_taster = pygame.key.get_pressed()

    sisten.flytt(trykkede_taster)
    haren.flytt(trykkede_taster)

    sisten.gradvisFartstap()

    sisten.tegnFirkant()
    haren.tegnFirkant()
    nektar.tegnFirkant()

    sisten.kollisjonsdeteksjon(haren)

    sisten.endreFartEtterNektar()
    haren.endreFartEtterNektar()

    for i in range (len(vegger)):
        vegger[i].tegnFirkant()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #sjekker om du har trykket på QUIT knappen , deretter gjør kjor false, noe som ender while løkken
            kjor = False

    pygame.display.flip() #oppdater vinduet med informasjonen gitt
    clock.tick(60)
    
