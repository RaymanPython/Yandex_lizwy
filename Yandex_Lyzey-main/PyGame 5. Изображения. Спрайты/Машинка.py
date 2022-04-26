import sys

import pygame
from pygame.locals import *


class Car(object):
    def __init__(self):
        self.image = pygame.image.load('car2.png')
        self.x = 95 // 2
        self.y = 95 // 2
        self.cor = 10

    def draw(self, surface):
        self.x += self.cor
        if self.x <= 0 or self.x >= 600:
            self.cor *= -1

        surface.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def move(self, xd, yd):
        self.x += xd * 10
        self.y += yd * 10


pygame.init()
screen = pygame.display.set_mode((600, 95))
cat = Car()
Clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    cat.draw(screen)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # If pressed key is ESC quit program
            if event.key == pygame.K_UP:
                cat.move(0, -1)
            if event.key == pygame.K_DOWN:
                cat.move(0, 1)
            if event.key == pygame.K_LEFT:
                cat.move(-1, 0)
            if event.key == pygame.K_RIGHT:
                cat.move(1, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    Clock.tick(40)
