a = input().split(' -> ')
n = int(input())
pos = []
dl = len(a) - 1
for i in range(n):
    s = input()
    pos.append(s)
for i in pos:
    f = a.index(i)
    x = f - 1
    y = f + 1
    if x >= 0 and y <= dl:
        print(a[x] + ' -> ' + i + ' -> ' + a[y])
    if x < 0 and y <= dl:
        print(i + ' -> ' + a[y])
    if x >= 0 and y > dl:
        print(a[x] + ' -> ' + i)
        print(a[x] + ' -> ' + i)
