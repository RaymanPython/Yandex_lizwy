a = []
for i in range(int(input())):
    a.append(input().split(','))
for i in range(int(input())):
    x, y = map(int, input().split(','))
    print(a[x][y])
