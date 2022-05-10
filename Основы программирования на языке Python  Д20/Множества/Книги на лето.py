m = int(input())
n = int(input())
a = set()
for i in range(m):
    a.add(input())
for i in range(n):
    if input() in a:
        print('YES')
    else:
        print('NO')
