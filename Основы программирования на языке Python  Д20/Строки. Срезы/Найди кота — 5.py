n = int(input())
x = 0
for i in range(n):
    a = input()
    x = 0
    if 'кот' in a or 'Кот' in a:
        for j in a:
            if j == 'к' and a[x + 1] == 'о':
                print(i + 1, x + 1)
            else:
                x += 1
