import pygame

WIDTH = 1000  # ширина игрового окна
HEIGHT = 1000  # высота игрового окна
FPS = 50  # ч
# астота кадров в секунду
YELLOW = pygame.Color('yellow')
BLUE = pygame.Color('blue')


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)
        self.color = YELLOW
        self.r = 50
        self.k = 0
        self.vx = 10
        self.vy = 10
        self.wx, self.wy = size
        self.pos = pos
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        x, y = self.rect.center
        wx = self.wx - self.r
        # x -= self.r
        wy = self.wy - self.r
        # y -= self.r
        if x - self.r < 0 or x + self.r > wx:
            self.vx *= -1
            print(x, y)

        if y - self.r < 0 or y + self.r > wy:
            self.vy *= -1
            print(x, y)
        x += self.vx
        y += self.vy
        self.rect.center = (x, y)


def main():
    pygame.init()
    pygame.mixer.init()  # для звука

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    screen.fill(BLUE)
    all_sprites = pygame.sprite.Group()
    # player = Player((50, 50))
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
                # screen.fill(BLUE)
                # all_sprites = pygame.sprite.Group()
                player = Player(event.pos, (WIDTH, HEIGHT))
                all_sprites.add(player)

        all_sprites.update()

        # Рендеринг
        screen.fill(BLUE)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


main()
