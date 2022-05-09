a = [0] * 4
b = [[True, True], [False, True], [False, False], [True, False]]
for i in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        print((x, y))
    else:
        for j in range(4):
            if ((x > 0) == b[j][0]) and ((y > 0) == b[j][1]):
                a[j] += 1
                break
for i in range(3):
    print('I' * (i + 1) + ':', a[i], end=', ')
print('IV' + ':', a[3], end='.')
