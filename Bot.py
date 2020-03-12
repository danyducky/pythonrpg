import pygame
import random
import Mob
from Hero import *
from Constants import *
from Objects import *
from Main import *
from Walls import *

class OutBot:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed-1
        self.counter = 0
        self.status= True


    def render(self, Player):
        if Player.dies < 10:
            screen.blit(self.image[self.direction][self.counter//4], (self.x,self.y))

    def move(self):
        self.block_check()
        if self.moves[right] == 1:
            self.direction = right
            self.x += self.speed
            self.counter += 1
            if self.counter == 16:
                self.counter = 0
        if self.moves[left] == 1:
            self.direction = left
            self.x -= self.speed
            self.counter += 1
            if self.counter == 16:
                self.counter = 0
        if self.moves[up] == 1:
            self.y -= self.speed
            self.direction = up
            self.counter += 1
            if self.counter == 16:
                self.counter = 0
        if self.moves[down] == 1:
            self.y += self.speed
            self.direction = down
            self.counter += 1
            if self.counter == 16:
                self.counter = 0

    def block_check(self):
        if self.x <= 710:
            self.x = 710
            self.moves = [1, 0, 0, 0]
        if self.x >=768:
            self.x = 768
            self.moves = [0, 1, 0, 0]
        if self.y <= 400:
            self.y = 400
            self.moves = [0, 0, 0, 1]
        if self.y >= 458:
            self.y = 458
            self.moves = [0, 0, 1, 0]

    def rand_move(self):
        if self.status == True:
            self.moves = [0,0,0,0]
            self.moves[random.randint(0,3)] = 1
class Milena(OutBot):
    def __init__(self, x, y, direction, speed):
        self.image = bot_imgs
        self.moves = [0,0,0,0]
        OutBot.__init__(self, x, y, direction, speed)
