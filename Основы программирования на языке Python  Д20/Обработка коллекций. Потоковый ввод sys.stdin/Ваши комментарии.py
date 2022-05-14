import sys

n = 0
for i in sys.stdin:
    s = i.rstrip('/n')
    a = s.split()
    if len(a) > 0:
        if a[0][0] == '#':
            n += 1
print(n)
