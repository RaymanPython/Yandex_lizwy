n = int(input())
i = 0
s = 0
for i in range(n):
    if n % (i + 1) == 0:
        print(i + 1, end=' ')
        s += 1
print()
if s > 2 or n == 1:
    print('НЕТ')
else:
    print('ПРОСТОЕ')
