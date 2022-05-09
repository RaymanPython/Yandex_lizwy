import pygame

# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 200, 200
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)

running = True
k = 0

while running:
    # внутри игрового цикла ещё один цикл
    # приёма и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
        if event.type == pygame.VIDEOEXPOSE:
            k += 1
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(str(k), 1, (100, 255, 100))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
