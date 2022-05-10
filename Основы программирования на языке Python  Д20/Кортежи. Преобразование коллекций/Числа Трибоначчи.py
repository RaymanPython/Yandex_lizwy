n = int(input())
a = [1, 1, 1]
for _ in range(n - 3):
    a.append(sum(a[-3:]))
print(*a[0: n])
