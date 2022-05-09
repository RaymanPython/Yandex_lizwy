import pygame

try:
    n = int(input())
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
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Сфера")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    for i in range(n):
        pygame.draw.ellipse(screen, WHITE, (0, 150 - (i + 1) * (150 // n), 300, (i + 1) * (300 // n)), 1)
        pygame.draw.ellipse(screen, WHITE, (150 - (i + 1) * (150 // n), 0, (i + 1) * (300 // n), 300), 1)
    pygame.display.flip()
pygame.quit()
