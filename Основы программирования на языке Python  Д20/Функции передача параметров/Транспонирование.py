def transpose(matrix):
    matrix[:] = tuple(zip(*matrix))
