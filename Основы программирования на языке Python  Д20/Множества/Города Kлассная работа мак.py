a = set()
n = int(input())
for i in range(n):
    a.add(input())
a.add(input())
if len(a) == n + 1:
    print('OK')
else:
    print('TRY ANOTHER')
