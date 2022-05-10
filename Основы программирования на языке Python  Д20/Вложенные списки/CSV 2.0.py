a = []
for i in range(int(input())):
    stroka = input().split(',')
    a.append(stroka)
for i in range(int(input())):
    x, y = map(int, input().split(','))
    print(a[x][y])
