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
pygame.display.set_caption("Ромбики")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('yellow'))
    for i in range(300 // n):
        for j in range(300 // n):
            cx, cy = i * n + n // 2, j * n + n // 2
            pygame.draw.polygon(screen, pygame.Color('orange'),
                                [[cx - n // 2, cy], [cx, cy + n // 2],
                                 [cx + n // 2, cy], [cx, cy - n // 2]])
    pygame.display.flip()
pygame.quit()
