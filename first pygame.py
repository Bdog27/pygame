import pygame
import random

WIDTH  = 580
HEIGHT = 780
FPS = 60

#colors rgb
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(White)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    def update (self):
        self.rect.y += -5
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
            

pygame.init() #create window
pygame.mixer.init() #sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))#screen
pygame.display.set_caption("Game") #Game name
clock = pygame.time.Clock()#keeps track of speed

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#game loop

running = True
while running:
    clock.tick(FPS)# keep loop running at right speed
    #processes inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #updates
    all_sprites.update()
    
    #reders
    screen.fill(Black)
    all_sprites.draw(screen)
    #after drawing everything flip dispplay
    pygame.display.flip()

pygame.quit()    
