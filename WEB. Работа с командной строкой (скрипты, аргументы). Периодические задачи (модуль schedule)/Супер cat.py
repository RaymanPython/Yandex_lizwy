import sys

for i in sys.argv:
    if len(i.split('.')) == 2 and i.split('.')[1] == 'txt':
        name = i
try:
    sys.stdin = open(name, 'r')
    x = 0
    f = '--count' in sys.argv
    f1 = '--num' in sys.argv
    f2 = '--sort' in sys.argv
    a = []
    for i in sys.stdin:
        if i.rstrip() == '':
            break
        a.append(i.rstrip())
    if f2:
        a.sort()
    for i in range(len(a)):
        if f1:
            print(i, a[i])
        else:
            print(a[i])
    if f:
        print(f'rows count: {len(a)}')
except FileNotFoundError or NameError:
    print('ERROR')
