import sys

s = 0
n = 0
for i in sys.stdin:
    s += int(i.rstrip('/n'))
    n += 1
if n == 0:
    print(-1)
else:
    print(s / n)
    ы
