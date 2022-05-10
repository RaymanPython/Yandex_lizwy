a = input()
s = a[0]
a = a[1:].split('V')
x = 0
for i in a:
    if len(i) != 0:
        if i[0] == '<':
            x -= len(i)
    print(' ' * x + s * (1 + len(i)))
    if len(i) != 0:
        if i[0] == '>':
            x += len(i)
