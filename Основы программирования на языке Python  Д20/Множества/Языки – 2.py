a = set()
b = set()
n = int(input())
m = int(input())
k = int(input())
x = 0
for i in range(n + m + k):
    s = input()
    if s in a:
        x += 1
        b.add(s)
    a.add(s)
if (n == k == m) and len(a) == n:
    print('NO')
else:
    if len(b) + x > 0:
        if ((len(b) + x) % 2 != 0):
            print((len(b) + x) % 2)
        else:
            print((len(b) + x) // 2)
    else:
        print('NO')
