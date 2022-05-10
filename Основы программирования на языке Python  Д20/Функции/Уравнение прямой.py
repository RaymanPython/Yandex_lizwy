def equation(a, b):
    x1, y1 = map(float, a.split(';'))
    x2, y2 = map(float, b.split(';'))
    if x2 == x1:
        print(x1)
    elif y1 == y2:
        print(y1)
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        print(k, b)
