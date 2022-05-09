import pygame

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Кирпичи")
clock = pygame.time.Clock()
running = True
w = 30
h = 15
n = 200 // (h + 2) + 1
m = 300 // (w + 2) + 1
y = 0
clock.tick(FPS)
if True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('WHITE'))
    for i in range(n):
        if i % 2 == 0:
            x = 0
        else:
            x = -w // 2
        for j in range(m):
            pygame.draw.rect(screen, RED, (x, y, w, h))
            x += w + 2
        y += h + 2
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()
