import pygame

# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 501, 501
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)

c = '(2;-1), (3,5;0,5), (4;-1), (5;0), (4;2), (2;1), (2;3), (4;5), (4;6), (2;5), (1;7), (1;8), (0;7), (0;9), (-1;7), (-2;8), (-2;7), (-3;7), (-2;6), (-4;6), (-3;5), (-4;5), (-3;4), (-5;4), (-4;3), (-5;3), (-4;2), (-6;2), (-5;1), (-6;1), (-5;0), (-6;0), (-5;-1), (-6;-2), (-4;-2), (-5;-3), (-3;-4), (-4;-5), (-2;-5), (-1;-6), (3;-6), (3;-5), (1;-5), (1;-4), (2;-3), (2;-1)'
c = list(map(eval, c.replace(',', '.').replace(';', ',').split('. ')))

running = True
zoom = 1

while running:
    # внутри игрового цикла ещё один цикл
    # приёма и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
            # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            zoom += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            zoom -= 1

        cz = []
        for p in c:
            cz.append((width // 2 + p[0] * zoom, height // 2 - p[1] * zoom))

        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, pygame.Color('red'), cz, 1)

        pygame.display.flip()
