import sys

import pygame
from pygame.locals import *


class Cat(object):
    def __init__(self):
        self.image = pygame.image.load('arrow.png')
        self.x = 1
        self.y = 1

    def draw(self, surface):
        mosx = 0
        mosy = 0
        x, y = pygame.mouse.get_pos()
        mosx = (x - self.x)
        mosy = (y - self.y)
        self.x = 0.9 * self.x + mosx
        self.y = 0.9 * self.y + mosy
        surface.blit(self.image, (self.x, self.y))
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((800, 600))
cat = Cat()
Clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    cat.draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    Clock.tick(40)
