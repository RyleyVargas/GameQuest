# This file was created by: Ryley Vargas


import pygame as pg
from threading import *
from time import *
from pygame.sprite import Group
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # this starts the game window 
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        # this part shiuld start a new game to play
        self.all_sprites = Group()
        self.platforms = Group()
        self.monsters = Group()
        self.platcount = 0
        self.projectiles = Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(self, 0, HEIGHT-40, WIDTH, 40)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        print(*self.platforms)
        self.tempGroup = Group()
        
        for plat in range(0, 10):
            if len(self.platforms) < 2:
                plat = Platform(self, random.randint(0,WIDTH-100), random.randint(0,HEIGHT-100), 100, 15)
                self.platforms.add(plat)
                self.all_sprites.add(plat)
                
            while True:
                newPlat = Platform(self, random.randint(0,WIDTH-100), random.randint(0,HEIGHT-100), 100, 15)
                self.tempGroup.add(newPlat)
                selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                if not selfCollide and not allCollide:
                    self.platforms.add(newPlat)
                    self.all_sprites.add(newPlat)
                    self.tempGroup.remove(newPlat)
                    
                    break

        self.run()
    def platGen(self, count):
        while count > 0:
            newPlat = Platform(self, random.randint(0,WIDTH-100), random.randint(-25, 0), 100, 15)
            self.tempGroup.add(newPlat)
            selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
            allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
            if not selfCollide and not allCollide:
                self.platforms.add(newPlat)
                self.all_sprites.add(newPlat)
                self.tempGroup.remove(newPlat)
                count = count-1
                
                break
    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        # Update - listen to see if anything changes...
        self.all_sprites.update()
        for p in self.projectiles:
            # print(p.birth)
            if p.rect.y < 0:
                p.kill()
                # print(self.projectiles)
        phits = pg.sprite.groupcollide(self.projectiles, self.platforms, False, False)
        if phits:
            pass
            # print("a projectile collided with a plat...")
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if self.player.rect.top > hits[0].rect.top:
                # print("i hit my head")
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top+1
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    print(len(self.platforms))
        while len(self.platforms) < 10:
            self.platGen(1)     
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()
    def show_start_screen(self):
        # game splash/start screen
        pass
    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
