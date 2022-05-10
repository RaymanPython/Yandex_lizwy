def squared(start, end, div):
    s = ''
    for k in range(start, end + 1):
        if (k ** 2 % div != 0):
            s += str(k ** 2) + ' ' * (5 - len(str(k ** 2)))
        if (k + 1) % 10 == start % 10:
            s += '\n'
    print(s)
