import pygame

try:
    a, n = map(int, input().split())
    if a % n != 0:
        a /= 0
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
screen = pygame.display.set_mode((a, a))
pygame.display.set_caption("Шахматная клетк")
clock = pygame.time.Clock()
running = True
color = n % 2 == 1
colors = []
for _ in range(n):
    col = []
    colx = color
    for _ in range(n):
        col.append(colx)
        colx = not colx
    colors.append(col)
    color = not color
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    for i in range(n):
        for j in range(n):
            if not colors[i][j]:
                pygame.draw.rect(screen, WHITE, (i * a // n, j * a // n, a // n, a // n))
    pygame.display.flip()
pygame.quit()
