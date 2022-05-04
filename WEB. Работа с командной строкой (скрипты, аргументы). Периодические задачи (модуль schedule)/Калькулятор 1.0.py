import sys

try:
    a = list(map(int, sys.argv[1:]))
    if len(a) == 2:
        print(sum(a))
    else:
        print(0)
except ValueError:
    print(0)
