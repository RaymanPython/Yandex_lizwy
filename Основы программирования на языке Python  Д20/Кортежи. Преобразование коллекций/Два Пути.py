a = []
b = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
    b.append(x)
n = int(input())
for i in range(n):
    c = int(input())
    d = int(input())
    x = int(input())
    if c == 1:
        a[d] = a[d] + x
    else:
        b[d] = b[d] + x
print(' '.join(map(str, a)))
print(' '.join(map(str, b)))
x = 0
for i in range(len(a)):
    if a[i] == b[i]:
        x += 1
print(x)
