import pygame

try:
    WIDTH, HEIGHT = map(int, input().split())
except:
    print('Неправильный формат ввода')
    quit()
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прямоугольник")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (1, 1, WIDTH - 2, HEIGHT - 2))
    pygame.display.flip()
pygame.quit()
