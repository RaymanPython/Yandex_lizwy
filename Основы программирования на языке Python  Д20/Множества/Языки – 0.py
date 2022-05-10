a = set()
x = 0
y = 0
n = int(input())
m = int(input())
for i in range(n):
    a.add(input())
for i in range(m):
    x = len(a)
    a.add(input())
    if x == len(a):
        y = y + 1
if len(a) - y == 0:
    print('NO')
else:
    print(len(a) - y)
