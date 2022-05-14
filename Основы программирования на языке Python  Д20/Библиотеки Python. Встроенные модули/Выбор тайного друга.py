import sys
import random

x1 = 1
group = list(map(str.strip, sys.stdin))
random.shuffle(group)
for main in range(0, len(group)):
    if main == len(group) - 1:
        print(group[main], ' - ', group[0])
    else:
        print(group[main], ' - ', group[x1])
        x1 += 1
