m = int(input())
n = int(input())
for i in range(n):
    for j in range(m):
        print((j + 1) / (i + 1), end=' ')
    print()
