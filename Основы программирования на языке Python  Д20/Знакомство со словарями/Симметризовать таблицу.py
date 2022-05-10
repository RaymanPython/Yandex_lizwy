n = int(input())
a = [[]]
for i in range(n - 1):
    s = input()
    a.append(s.split())
for i in range(n):
    s = ''
    for j in range(n):
        if i == j:
            s += '0 '
        elif j < i:
            s += a[i][j] + ' '
        else:
            s += a[j][i] + ' '
    print(s)
