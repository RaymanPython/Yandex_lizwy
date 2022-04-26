import pygame

if __name__ == '__main__':
    global pos
    pygame.init()

    width, height = 500, 500
    size = width, height
    screen = pygame.display.set_mode(size)

    running = True
    state1 = 0
    state2 = 1
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                state1 = 0
                state2 = 0
        while state2 != 1:
            pygame.draw.circle(screen, (255, 255, 0), pos, state1)
            state1 += 10
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    state2 = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill((0, 0, 255))
                    pygame.display.flip()
                    pos = event.pos
                    state1 = 0
    pygame.quit()
