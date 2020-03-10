import pygame
from Constants import *
from Hero import *
class fireball:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.image = fireball_imgs
        self.direction = direction
        self.firespeed = speed
        self.mob_x = x
        self.mob_y = y

    def render(self, fireball, fireballs):
        if self.x <= width and self.x >= 0:
            screen.blit(self.image[self.direction], (self.x, self.y))
        else:
            fireballs.remove(fireball)
        if self.y >= 0 and self.y <= height:
            screen.blit(self.image[self.direction], (self.x, self.y))
        else:
            fireballs.remove(fireball)

    def move(self):
        if self.direction == right:
            self.x += self.firespeed
        elif self.direction == left:
            self.x -= self.firespeed
        elif self.direction == up:
            self.y -= self.firespeed
        else:
            self.y += self.firespeed

    def hud_contact(self, fireball, fireballs):
        try:
            if self.x < 310  and self.y >= height - 80:
                self.x = 310
                fireballs.remove(fireball)
            if self.y > height - 80 and self.x < 310:
                self.y = height - 80
                fireballs.remove(fireball)
            if self.x < 110 and self.y > height - 110:
                self.x = 110
                fireballs.remove(fireball)
            if self.y > height- 130 and self.x < 110:
                self.y = height- 130
                fireballs.remove(fireball)
        except:
            pass

        try:
            if 100 < self.x < 270 and 490 < self.y < 520:
                fireballs.remove(fireball)
            if 100 < self.x < 280 and 480 < self.y < 520:
                fireballs.remove(fireball)
        except:
            pass

class Fire(fireball):
    def __init__(self, x, y, direction, speed):
        fireball.__init__(self, x, y, direction, speed)
        self.image = fire
