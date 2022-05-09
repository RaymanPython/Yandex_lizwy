import pygame

try:
    w, n = map(int, input().split())
except:
    print('Мишень')
    quit()
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((2 * w * n, 2 * w * n))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
colors = [RED, GREEN, BLUE]
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    for i in range(n):
        pygame.draw.circle(screen, colors[i % 3],
                           (w * n, w * n), w * (i + 1), w)
    pygame.display.flip()
pygame.quit()
