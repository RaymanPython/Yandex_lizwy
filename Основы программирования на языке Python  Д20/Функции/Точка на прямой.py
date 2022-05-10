def line(s, t):
    a, b = map(float, s.split('x'))
    x, y = map(float, t.split(';'))
    print(a * x + b == y)
