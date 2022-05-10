k = 1
s = 2
n = int(input())
for i in range(n):
    print(i + 1, end=' ')
    k -= 1
    if k <= 0:
        print()
        k = s
        s += 1
