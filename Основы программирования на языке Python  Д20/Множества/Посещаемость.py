m = int(input())
a = set()
n = int(input())
for i in range(n):
    a.add(input())
for i in range(m - 1):
    n = int(input())
    b = set()
    for j in range(n):
        b.add(input())
    a &= b
for i in a:
    print(i)
