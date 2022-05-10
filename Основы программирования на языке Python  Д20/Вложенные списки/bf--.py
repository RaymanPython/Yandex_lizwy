s = input()
n = 30000
a = [0] * n
k = 0
for i in s:
    if i == '<':
        k = (k - 1) % n
    elif i == '>':
        k = (k + 1) % n
    elif i == '+':
        a[k] = (a[k] + 1) % 256
    elif i == '-':
        a[k] = (a[k] - 1) % 256
    else:
        print(a[k])
