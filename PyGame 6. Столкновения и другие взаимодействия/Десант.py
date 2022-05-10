import pygame

pygame.init()
width, height = 300, 78
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Десант')

BLACK = (0, 0, 0)


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load("mountains.png")

    def init(self):
        super().init(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = pygame.image.load("pt.png")

    def init(self, pos):
        super().init(all_sprites)

        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def Update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


all_sprites = pygame.sprite.Group()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)
    mountain = Mountain()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.Update()
    pygame.display.flip()

pygame.quit()
