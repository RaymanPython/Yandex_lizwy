n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(1, n):
    print(a[i] + a[i - 1])
