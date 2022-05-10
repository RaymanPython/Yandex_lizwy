a = set()
b = set()
x = 0
k = 0
n = int(input())
for i in range(n):
    s = input()
    a.add(s)
    if len(a) == x:
        k += 1
        b.add(s)
    x = len(a)
print(k + len(b))
