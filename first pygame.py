import pygame
import random
from os import path

WIDTH  = 580
HEIGHT = 780
FPS = 60

#colors rgb
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

pygame.init() #create window
pygame.mixer.init() #sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))#screen
pygame.display.set_caption("Game") #Game name
clock = pygame.time.Clock()#keeps track of speed

img_dir = path.join(path.dirname(__file__),"whateveryouwantbuddy")
player_img = pygame.image.load(path.join(img_dir, "Red_Guy.png")).convert()
mob_img = pygame.image.load(path.join(img_dir, "Meteor.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "Laser.png")).convert()


font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, White)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    





    
class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image = pygame.transform.scale(player_img,(30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT-10)
    def update (self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(4, 7)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(4, 7)
            self.speedx = random.randrange(-3, 3)
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -4
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <0:
            self.kill()

bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
score = 0








#game loop

running = True
while running:
    clock.tick(FPS)# keep loop running at right speed
    #processes inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
             player.shoot()
    #updates
    all_sprites.update()
    
    hits = pygame.sprite.groupcollide(mobs, bullets, True,False)
    for hit in hits:
        score += 100
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
        
    #reders
    screen.fill(Black)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 20, WIDTH/2, 10)
    #after drawing everything flip dispplay
    pygame.display.flip()

pygame.quit()    
