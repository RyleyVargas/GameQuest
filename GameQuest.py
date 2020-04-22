# This file was created by: Ryley Vargas
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 
'''
Lore for the week:
Functions, methods, Classes, scope('global' vs local)
For loops, break, pass, % modulu, 
string and list traversal
'''

# import libs
import pygame
import random
import os
from pygame.sprite import Sprite

# global variables
RUNNING = True
# screen dims
WIDTH = 800
HEIGHT = 600
# frames per second
FPS = 30
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
REDDISH = (240,64,64)
GREEN = (64,230,64)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pygame.mouse.get_pos()
    return (x,y)

# classes for game

class Player(Sprite):
    # sprite for player
    # properties of the class
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(BLACK)
        '''sets image path to correct location joining image folder to file name then converting to a more efficient format'''
        # self.image = pygame.image.load(os.path.join(img_folder, "Tie.png")).convert()
        '''sets transparent color key to black'''
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.screen_rect = screen.get_rect()
        self.vx = 0
        self.vy = 0
        self.cofric = 0.5
    # stuff it can do....
    def friction(self):
        # print("friction...")
        # if self.vx > -0.5 or self.vx < 0.5:
        #     print("velocity is in range...")
        #     self.vx = 0
        if self.vx > 0.5:
            self.vx -= self.cofric
        elif self.vx < -0.5:
            self.vx += self.cofric
        else:
            self.vx = 0
        if self.vy > 0.5:
            self.vy -= self.cofric
        elif self.vy < -0.5:
            self.vy += self.cofric
        else:
            self.vy = 0
    def update(self):
        # print(self.vx)
        self.friction()
        # self.vy += 9.8
        self.rect.x += self.vx
        self.rect.y += self.vy
        # if self.rect.right > WIDTH:
        #     self.rect.x = -50
        #     print("running off screen")
        # if self.rect.top > 500:
        #     self.vy = -5
        # if self.rect.top < 100:
        #     self.vy = 5
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.vy -= 5
        if keystate[pygame.K_a]:
            self.vx -= 5
        if keystate[pygame.K_s]:
            self.vy += 5
        if keystate[pygame.K_d]:
            self.vx += 5
        # if keystate[pygame.K_SPACE]:
        #     self.shoot()
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            # print("touched the right side...")
        if self.rect.left < 0:
            self.rect.left = 0
            # print("touched the left side...")
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            # print("touched the bottom")
        if self.rect.top < 0:
            self.rect.top = 0
            # print("touched the top")
    def jump(self):
        print("I jumped...")
        
   def gravity(self):
        self.cofric += 3.2 # how fast player falls
       
        if self.cofric.y > worldy and self.cofic >= 0:
            self.cofric  = 0
            self.rect.y = worldy-ty-ty
       
class Enemy(Sprite):
    # sprite for player
    # properties of the class
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)
        '''sets image path to correct location joining image folder to file name then converting to a more efficient format'''
        # self.image = pygame.image.load(os.path.join(img_folder, "Tie.png")).convert()
        '''sets transparent color key to black'''
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.screen_rect = screen.get_rect()
        self.vx = 5
        self.vy = 5
        self.cofric = 0.5
    # stuff it can do....
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right > WIDTH:
            self.vx*=-1
            self.rect.y += 10
            self.rect.x = WIDTH - 50
        if self.rect.left < 0:
            self.vx*=-1
            self.rect.y += 10
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

    def jump(self):
        print("I jumped...")

# init pygame and create window
pygame.init()
# init sound mixer
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game...")
clock = pygame.time.Clock() 

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
# testSprite = Sprite()
# testSprite.image = pygame.Surface((50,50))
# testSprite.image.fill(GREEN)
# testSprite.rect = testSprite.image.get_rect()
# testSprite.rect.center = (WIDTH / 2, HEIGHT / 2)
all_sprites.add(player)
# all_sprites.add(testSprite)

for i in range(0,100):
    print(i)
    i = Enemy()
    i.rect[0] = random.randint(0,WIDTH-25)
    i.rect[1] = random.randint(0,HEIGHT)
    enemies.add(i)
    all_sprites.add(i)

# game loop

while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pygame.event.get():
        # check for window closing
        if event.type == pygame.QUIT:
            RUNNING = False
    
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
    all_sprites.update()

    blocks_hit_list = pygame.sprite.spritecollide(player, enemies, True)
    for block in blocks_hit_list:
        print("collided")
    ### draw and render section of game loop
    screen.fill(REDDISH)
    all_sprites.draw(screen)
    # double buffering draws frames for entire screen
    pygame.display.flip()
    # pygame.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pygame.quit()
