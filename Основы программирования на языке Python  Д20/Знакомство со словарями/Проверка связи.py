s = input().split()
a = dict()
for i in s:
    if i in a.keys():
        a[i] = a[i] + 1
    else:
        a[i] = 1
    print(a[i], end=' ')
