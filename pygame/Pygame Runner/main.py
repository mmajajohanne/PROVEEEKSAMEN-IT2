from distutils.errors import DistutilsGetoptError
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):  #arver fra en pygame klasse
    def __init__(self):
        super().__init__() #access the Sprite class
        

        player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0 #use to pick either 1 or 2
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()


        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self): #en metode
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
            
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index] #always needed
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))#always needed
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self): #fjerner alle hindirnger som ligger ca. utenfor skjermen
        if self.rect.x <= -100: 
            self.kill()

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000) #millisekunder, recrods the time from when init() was run
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -= 5
            if obstacle_rectangle.bottom == 300:
                screen.blit(snail_surface,obstacle_rectangle)
            else:
                screen.blit(fly_surface,obstacle_rectangle)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #Setter listen lik alle hindrene som har x-kordinat høyere enn -100. Altså så lenge de vises på skjermen. Slik unngår vi å få et uendelelig antall hindre
        return obstacle_list
        
    else: return []

def collisions(player,obstacles): #returns true or false, then we make game_actve that value
    if obstacles:
        for obstacle_rectangle in obstacles:
            if player.colliderect(obstacle_rectangle):
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty() #fjerner alle hindringene og starter med helt blank bane
        return False
    else:
        return True

def player_animation():
    global player_surface, player_index #gjør at funskjonen påvirker globale variabler

    if player_rectangle.bottom < 300: #while above ground, he is jumping
        player_surface = player_jump #changes the image of the player so that it looks like he jumped
    else:
        player_index += 0.1 #makes the transition slower bewteen walking surfaces
        if player_index >= len(player_walk): player_index = 0 #begrenser slik at det ikke overstiger lengden på arrayen.
        player_surface = player_walk[int(player_index)]

    #play wlaking animaton when person is on floor
    #display the jump when player is not on the floow

pygame.init() #starts pygame run images and sounds you just need to make it start running
screen = pygame.display.set_mode((800,400)) #lager den svarte ruten du skal spille i
pygame.display.set_caption("Runner") #gir vinduet en tittel
clock = pygame.time.Clock() #gives a clock object
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #(font type,font size)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.5)
bg_music.play(loops = -1) #tells pygame to play forever

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

score_surface = test_font.render('My game', False, (64,64,64)) #(text, smoothing, colour)
score_rectangle = score_surface.get_rect(center = (400,50))

player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0 #use to pick either 1 or 2
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surface = player_walk[player_index]

player_rectangle = player_surface.get_rect(midbottom = (80,300)) #makes a rect that is the same size as player, tehn we can grab any points and placee them where we want.
player_gravity = 0
#intro
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rectangle = player_stand.get_rect(center = (400,200))

# obstacles
snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0

fly_frame1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame1, fly_frame2]

fly_frame_index = 0

obstacle_rectangle_list = []

sky_surface = pygame.image.load('graphics/Sky.png').convert()
#every new graphical element is a new surface
ground_surface = pygame.image.load('graphics/ground.png').convert()

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rectangle = game_name.get_rect(center = (400,80))

game_message_surface = test_font.render('Press space to start',False,(111,196,169))
game_message_rectangle = game_message_surface.get_rect(center = (400,330))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # creates events by using userevent + an index to differenciate
pygame.time.set_timer(obstacle_timer,1500) # Sends out an event signal named obstacle_timer every 1.5 second. Which makes it a timer that goes off every 1.5 seconds essencially. 

snail_animation_timer = pygame.USEREVENT + 2 
pygame.time.set_timer(snail_animation_timer,500) #0.5 sek

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200) #0.2 sek


while True:
    for event in pygame.event.get(): #gets events
        if event.type == pygame.QUIT: #sjekker om du krysser ut av vinduet
            pygame.quit() #stenger vinduet, unaniciates everytinh 
            exit() #while løkken stoppes.

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
        if game_active:
            if event.type == obstacle_timer: #(gameactive true) #detects that the timer has gone off and does something for each time.
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
                """if randint(0,2): #gives 0/false or 1/true 
                    obstacle_rectangle_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rectangle_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))"""

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index] #changes the image of the obstacle. Alternates for every interval the timer is set to


    if game_active:
        screen.blit(sky_surface,(0,0)) #her sier vi at den skal ligge i origon (øverste venstre hjørne)
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        score = display_score()

        """screen.blit(snail_surface, snail_rectangle) #to move snail you need to move the rectangle
        snail_rectangle.x -= 4 #talks about position of rectangle from bottomright
        if snail_rectangle.right <= 0: snail_rectangle.left = 800 #talks about points on the rectangle (left n right)"""

        #if player_rectangle.colliderect(snail_rectangle):
            #detects collisions every frame n returns 1 when collision
        #mouse_position = pygame.mouse.get_pos()
        #if player_rectangle.collidepoint(mouse_po):
            #pygame.mouse.get_pressed()

        # Player
        """player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        player_animation()
        screen.blit(player_surface,player_rectangle) """
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

        #u need a background which is a surface that updates every frame, that way u wont be seeing the previous frames of a foreground element like the snail

        # Obstacle movement
        #obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list) #opdaterer listen for hver bevegelse

        # Collision
        # game_active = collisions(player_rectangle,obstacle_rectangle_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rectangle)
        screen.blit(game_name,game_name_rectangle)
        
        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rectangle = score_message.get_rect(center = (400,330))

        if score == 0:
            screen.blit(game_message_surface,game_message_rectangle)
        else:
            screen.blit(score_message,score_message_rectangle)

    # draw all our elements n update everyething
    pygame.display.update() #ikke kjør koden om kun dette er tilstede, da vil du ikke kunne lukke vinduet, no player input
    clock.tick(60) #while løkken må ikke kjøre mer enn 60 frames per second



