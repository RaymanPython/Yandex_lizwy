def f1(x):
    return int(x[1])


def f(x):
    return x[0]


def possible_turns(s):
    desk = 'ABCDEFGH'
    for i in range(8):
        if desk[i] == s[0]:
            y = i + 1
    x = int(s[1])
    a = []
    move = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    for yd, xd in move:
        if 0 < y + yd < 9 and 0 < x + xd < 9:
            a.append(desk[y + yd - 1] + str(x + xd))
    a = sorted(a, key=f1)
    a = sorted(a, key=f)
    return a
