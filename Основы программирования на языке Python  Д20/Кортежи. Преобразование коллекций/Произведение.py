n = int(input())
a = []
c = False
for i in range(n):
    a.append(int(input()))
x = int(input())
for i in range(n):
    for j in range(n):
        if a[i] * a[j] == x and i != j:
            c = True
            break
if c:
    print('ДА')
else:
    print('НЕТ')
