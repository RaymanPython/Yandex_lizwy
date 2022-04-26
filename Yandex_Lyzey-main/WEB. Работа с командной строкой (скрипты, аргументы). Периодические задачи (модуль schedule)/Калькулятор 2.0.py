import sys

try:
    a = list(map(int, sys.argv[1:]))
    if len(a) == 0:
        print(' NO PARAMS')
    else:
        s = 0
        for i in range(len(a)):
            if i % 2 == 0:
                s += a[i]
            else:
                s -= a[i]
        print(s)
except ValueError:
    print('ValueError')
