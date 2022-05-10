def triangle(a, b, c):
    s = a + b + c
    if s > 2 * a and s > 2 * b and s > 2 * c:
        print('Это треугольник')
    else:
        print('Это не треугольник')
