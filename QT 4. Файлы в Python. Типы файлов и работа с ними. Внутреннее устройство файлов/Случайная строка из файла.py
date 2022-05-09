import random

f = open('lines.txt', 'r')
flag = 0

for line in f:
    if flag == 0:
        line2 = line
        flag = 1
    elif random.randint(0, 1) == 1:
        line2 = line
if flag > 0:
    print(line2)
f.close()
