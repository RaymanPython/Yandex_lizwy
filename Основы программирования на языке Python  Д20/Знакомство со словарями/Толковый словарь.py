a = int(input())
s = 0
f = ''
slow = dict()
while s != a:
    x = input()
    for i in range(len(x)):
        if x[i] != ' ':
            f += x[i]
        else:
            break
    x = x.split()
    del x[0]
    slow[f] = x
    f = ''
    s += 1
b = int(input())
for _ in range(b):
    new = input()
    if new not in slow:
        print('Нет в словаре')
    else:
        print(*slow[new])
