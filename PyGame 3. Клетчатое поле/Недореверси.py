import pygame
import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color_matric = [[random.randint(1, 2) for j in range(height)] for i in range(width)]
        self.xod = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def krest(self, screen, x, y, size):
        pygame.draw.line(screen, pygame.Color(0, 0, 255), (x, y), (x + size, y + size), 2)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), (x, y + size), (x + size, y), 2)

    def zerol(self, screen, color, x, y, size):
        pygame.draw.circle(screen, color, (x + size // 2, y + size // 2), size // 2)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
                '''
                pygame.draw.rect(screen, color_c, (
                    x * self.cell_size + self.left + 1, y * self.cell_size + self.top + 1, self.cell_size - 2,
                    self.cell_size - 2), 0)
                '''
                if self.color_matric[x][y] == 1:
                    self.zerol(screen, pygame.Color(255, 0, 0), x * self.cell_size + self.left + 1,
                               y * self.cell_size + self.top + 1,
                               self.cell_size)
                elif self.color_matric[x][y] == 2:
                    self.zerol(screen, pygame.Color(0, 0, 255), x * self.cell_size + self.left + 1,
                               y * self.cell_size + self.top + 1,
                               self.cell_size)

    def mouse_cor(self, pos):
        x, y = pos
        x -= self.left
        y -= self.top
        x //= self.cell_size
        x += 1
        y //= self.cell_size
        y += 1
        if x > self.width or y > self.height or x == 0 or y == 0:
            return None
        else:
            return (x, y)

    def remove_color(self, pos):
        pos = self.mouse_cor(pos)
        # print(pos)
        if pos != None:
            x, y = pos
            x -= 1
            y -= 1
            if True:
                if self.xod:
                    for i in range(self.width):
                        self.color_matric[i][y] = 1
                    for j in range(self.height):
                        self.color_matric[x][j] = 1
                else:
                    for i in range(self.width):
                        self.color_matric[i][y] = 2
                    for j in range(self.height):
                        self.color_matric[x][j] = 2
                self.xod = not self.xod


def main():
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    n = int(input())
    board = Board(n, n)
    board.set_view(50, 50, 55)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.remove_color(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
