n = int(input())
r = 1
rr = []
dd = []
while r not in rr:
    rr.append(r)
    dd.append(str(10 * r // n))
    r = 10 * r % n
print(''.join(dd[rr.index(r):]))
