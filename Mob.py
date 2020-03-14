import pygame
import random
from Constants import *
from Objects import *
from Main import *
from Walls import *


class Mob:
    def __init__(self, x, y, direction, speed):
        self.moves = [0,0,0,0]
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.counter = 0
        self.status = True
        self.runstatus = False
        self.fireballs = []
        self.len_of_dem = len_of_demons
        self.dies = 0

    def render(self):
        if self.status == True:
            screen.blit(self.image[self.direction][self.counter // 6], (self.x, self.y))
        elif self.status == False:
            self.runstatus = True
            self.status = False
            self.moves = [0,0,0,0]
            screen.blit(pygame.image.load('data/demon_die.png'), (self.x, self.y))

    def render_shot(self, objects, Player):
        for fireball in self.fireballs:
            fireball.move()
            fireball.hud_contact(fireball, self.fireballs)
            fireball.render(fireball, self.fireballs)
            try:
                for wall in objects:
                    wall.fireball_contact(fireball, self.fireballs)
            except:
                pass
            for fireball in self.fireballs:
                if Player.status == True:
                    if fireball.x - 18 < Player.x < fireball.x + 18 and fireball.y - 18 < Player.y < fireball.y + 18:
                        self.fireballs.remove(fireball)
                        if Player.hp > 0:
                            Player.hp -= 50
                        if Player.hp <= 0:
                            Player.hp = 0
                            Player.hp_regen = 0
                            Player.mp_regen = 0
                            Player.status = False


    def move(self):
        self.block_check()
        if self.moves[right] == 1:
            self.direction = right
            self.x += self.speed
            self.counter += 1
            if self.counter == 36:
                self.counter = 0
        if self.moves[left] == 1:
            self.direction = left
            self.x -= self.speed
            self.counter += 1
            if self.counter == 36:
                self.counter = 0
        if self.moves[up] == 1:
            self.y -= self.speed
            self.direction = up
            self.counter += 1
            if self.counter == 36:
                self.counter = 0
        if self.moves[down] == 1:
            self.y += self.speed
            self.direction = down
            self.counter += 1
            if self.counter == 36:
                self.counter = 0

    def rand_move(self):
        if self.status == True:
            self.moves = [0,0,0,0]
            self.moves[random.randint(0,3)] = 1

    def block_check(self):
        if self.x <= 0:
            self.x = 0
            self.moves = [1,0,0,0]
        if self.x >= width - 32:
            self.x = width - 32
            self.moves = [0,1,0,0]
        if self.y <= 0:
            self.y = 0
            self.moves = [0,0,0,1]
        if self.y >= height - 48:
            self.y = height - 48
            self.moves = [0,0,1,0]


        if self.x < 310 and self.y >= height-105:
            self.x = 310
        if self.y > height-110 and self.x < 310:
            self.y = height-110

        if self.x < 110 and self.y > height - 150:
            self.x = 110
        if self.y > height - 155 and self.x < 110:
            self.y = height - 155

        if 100 < self.x < 260 and 450 < self.y < 520:
            self.y = 450
        if 100 < self.x < 270 and 465 < self.y < 505:
            self.x = 270


    def contact_wall(self, wall):
        if wall.x - 30 < self.x < wall.x + 20 and wall.y - 40 < self.y < wall.y + 30:
            self.x = wall.x - 30
            self.moves = [0,0,1,0]
        if wall.x - 30 < self.x < wall.x + 40 and wall.y - 40 < self.y < wall.y + 30:
            self.x = wall.x + 40
            self.moves = [0,0,random.choice([0,1]),1]
            if self.moves[2] == 1 and self.moves[3] == 1:
                self.moves = [0,0,0,0]
        if wall.x - 30 < self.x < wall.x + 40 and wall.y - 40 < self.y < wall.y + 42:
            self.y = wall.y + 42
            self.moves = [0,1,0,0]
        if wall.x - 30 < self.x < wall.x + 40 and wall.y - 50 < self.y < wall.y + 42:
            self.y = wall.y - 50
            self.moves = [1,0,0,0]

    def contact_tree(self, tree):
        if tree.x - 30 < self.x < tree.x + 20 and tree.y - 40 < self.y < tree.y + 30:
            self.x = tree.x - 30
            self.moves = [0, 0, 1, 0]
        if tree.x - 30 < self.x < tree.x + 30 and tree.y - 40 < self.y < tree.y + 30:
            self.x = tree.x + 30
            self.moves = [0, 0, random.choice([0, 1]), 1]
            if self.moves[2] == 1 and self.moves[3] == 1:
                self.moves = [0, 0, 0, 0]
        if tree.x - 30 < self.x < tree.x + 20 and tree.y - 40 < self.y < tree.y + 63:
            self.y = tree.y + 63
            self.moves = [1, 0, 0, 0]
        if tree.x - 30 < self.x < tree.x + 20 and tree.y - 50 < self.y < tree.y + 42:
            self.y = tree.y - 50
            self.moves = [0, 1, 0, 0]

    def draw_hp(self):
        if self.status == True:
            font_size = 12
            font = pygame.font.Font('data/font1.ttf', font_size)
            hp_render = font.render(str(self.hp), 1, (255, 0, 0))
            screen.blit(hp_render, (self.x + 8, self.y - 20))

    def fireball_contact(self, mobs, mob, fireballs, fireball, Player):
        if self.runstatus == False:
            try:
                if self.x - 32 <= fireball.x <= self.x + 32 and self.y-20 <= fireball.y <= self.y+48 :
                    fireballs.remove(fireball)
                    if self.hp > 0:
                        self.hp -= 50
                    if self.hp <= 0:
                        self.status = False
                        Player.score += 50
                        Player.dies += 1 # счетчик смертей ДЕМОНОВ / КОСТЫЛЬ
            except:
                pass


    def remove(self, mobs, mob):
        if self.status == False:
            ticks = pygame.time.get_ticks()
            if ticks > 11000:
                mobs.remove(mob)

    def shoot(self):
        if self.direction == right:
            self.fireballs.append(fireball(self.x + 5, self.y, right, fireball_speed))
        elif self.direction == left:
            self.fireballs.append(fireball(self.x - 5, self.y, left, fireball_speed))
        elif self.direction == up:
            self.fireballs.append(fireball(self.x + 5, self.y - 10, up, fireball_speed))
        elif self.direction == down:
            self.fireballs.append(fireball(self.x + 10, self.y + 10, down, fireball_speed))

class Demon(Mob):
    def __init__(self, x, y, direction, speed):
        self.image = demon_imgs
        self.moves = [0,0,0,0]
        self.hp = demon_hp
        self.smert = 0
        Mob.__init__(self, x, y, direction, speed)

class Bog(Mob):
    def __init__(self, x, y, direction, speed):
        self.image = bog_imgs
        self.moves = [0,0,0,0]
        self.hp = 1500
        Mob.__init__(self, x, y, direction, speed)

    def shoot(self):
        if self.direction == right:
            self.fireballs.append(Fire(self.x + 5, self.y, right, fire_speed))
        elif self.direction == left:
            self.fireballs.append(Fire(self.x -5, self.y, left, fire_speed))
        elif self.direction == up:
            self.fireballs.append(Fire(self.x, self.y - 10, up, fire_speed))
        elif self.direction == down:
            self.fireballs.append(Fire(self.x, self.y + 10, down, fire_speed))

    def fireball_contact(self, mobs, mob, fireballs, fireball, Player): # контакт моба с фирболом
        if self.runstatus == False:
            try:
                if self.x - 32 <= fireball.x <= self.x + 32 and self.y-20 <= fireball.y <= self.y+48 :
                    fireballs.remove(fireball)
                    if self.hp > 0:
                        self.hp -= 50
                    if self.hp <= 0:
                        self.status = False
                        Player.score += 50
            except:
                pass



    def render_shot(self, objects, Player):
        for fireball in self.fireballs:
            fireball.move()
            fireball.hud_contact(fireball, self.fireballs)
            fireball.render(fireball, self.fireballs)
            try:
                for wall in objects:
                    wall.fireball_contact(fireball, self.fireballs, objects, wall)
            except:
                pass
            for fireball in self.fireballs:
                if Player.status == True:
                    if fireball.x - 35 < Player.x < fireball.x + 35 and fireball.y - 35 < Player.y < fireball.y + 35:
                        self.fireballs.remove(fireball)
                        if Player.hp > 0:
                            Player.hp -= 100
                        if Player.hp <= 0:
                            Player.hp = 0
                            Player.hp_regen = 0
                            Player.mp_regen = 0
                            Player.status = False
