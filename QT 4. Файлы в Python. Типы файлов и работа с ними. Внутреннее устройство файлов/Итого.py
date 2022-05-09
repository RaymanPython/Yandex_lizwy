import random

f = open('prices.txt', 'r')
s = 0
for line in f:
    l, x, c = line.split()
    x = int(x)
    c = float(c)
    s += x * c
print(s)
f.close()
