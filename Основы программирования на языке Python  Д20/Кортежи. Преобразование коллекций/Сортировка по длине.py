def f(a, b):
    if len(a) == len(b):
        return a > b
    else:
        return len(a) > len(b)


n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n - 1):
    for j in range(n - i - 1):
        if f(a[j], a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
print('\n'.join(a))
