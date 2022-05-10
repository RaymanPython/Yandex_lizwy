m = 0
mi = 1
n = int(input())
for i in range(n):
    d = 100000000000
    for j in range(int(input())):
        x = int(input())
        if x < d:
            d = x
    if m < d:
        m = d
        mi = i + 1
print(mi, m)
