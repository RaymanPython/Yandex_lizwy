a = input().split()
s = ''
for i in range(len(a)):
    if i % 3 == 2:
        s += a[i] + ' '
print(s)
