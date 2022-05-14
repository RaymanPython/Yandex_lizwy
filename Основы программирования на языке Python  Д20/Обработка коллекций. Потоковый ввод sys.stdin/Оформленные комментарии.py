import sys

n = 1
for i in sys.stdin:
    s = i.rstrip('/n')
    a = s.split()
    if len(a) > 0:
        if a[0][0] == '#':
            s = ' '.join(a)
            s = s[1:]
            if s[0] == ' ':
                s = s[1:]
            print('Line', str(n) + ':', s)
    n += 1
