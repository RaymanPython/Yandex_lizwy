class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        elif result == 'sink':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if self.map[i][j] == '.':
                            self.map[i][j] = '*'
            self.map[row][col] = 'x'
            for j in range(len(self.map)):
                if self.map[row][j] == 'x':
                    col = j
                    for i in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= u < 10:
                                if self.map[i][u] == '.':
                                    self.map[i][u] = '*'
            for v in range(len(self.map)):
                if self.map[v][col] == 'x':
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if self.map[v][u] == '.':
                                    self.map[v][u] = '*'

    def cell(self, row, col):
        return self.map[row][col]
