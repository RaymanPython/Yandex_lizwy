n = int(input())
d = {}
for i in range(n):
    s = input().split('\t')
    if s[0] not in d:
        d[s[0]] = []
        d[s[0]].append(s[1])
    else:
        d[s[0]].append(s[1])
input()
a = 0
f = 1
g = 0
while True:
    b = input()
    if b == '.':
        a += g
        if g != 0:
            print(f'{f}) {g}')
        print(f'Итого: {a}')
        break
    if len(b) != 0:
        b = b.split('\t')
        g += int(d[b[0]][0]) * int(b[1])
    if len(b) == 0 and g != 0:
        a += g
        print(f'{f}) {g}')
        f += 1
        g = 0
