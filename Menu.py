import pygame
import Main

class menu:
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.render()


    def background():
        Main.screen.blit(pygame.image.load('data/invoker2.jpg'), (0,0))

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

    def text(text, size, coords=(0, 0), color=(255, 0, 0)):
        font = pygame.font.Font('data/font1.ttf', size)
        word = font.render(str(text), 1, color)
        Main.screen.blit(word, coords)
