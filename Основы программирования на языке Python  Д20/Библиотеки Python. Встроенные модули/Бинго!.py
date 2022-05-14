from random import shuffle
from pprint import pprint


def make_bingo():
    a = list(range(1, 75))
    shuffle(a)
    k = 0
    x = []
    for i in range(1, 6):
        if i == 3:
            x.append((a[k], a[k + 1], 0, a[k + 3], a[k + 4]))
            k += 5
            continue
        x.append((a[k], a[k + 1], a[k + 2], a[k + 3], a[k + 4]))
        k += 5
    return tuple(x)
