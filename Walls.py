import pygame
from Constants import *
from Objects import *

class Objects:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def fireball_contact(self, fireball, fireballs):
        try:
            if self.x - 20 <= fireball.x <= self.x + 32 and self.y - 12 <= fireball.y <= self.y + 34:
                fireballs.remove(fireball)
        except:
            pass




class Wall(Objects):
    def __init__(self, x, y):
        self.image = wall_image
        Objects.__init__(self, x, y)
class Tree(Objects):
    def __init__(self, x, y):
        self.image = tree_image
        Objects.__init__(self, x, y)

    def fireball_contact(self, fireball, fireballs):
        try:
            if self.x - 32 <= fireball.x <= self.x + 20 and self.y - 28 <= fireball.y <= self.y + 65:
                fireballs.remove(fireball)
        except:
            pass
