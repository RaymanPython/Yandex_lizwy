n = int(input())
for i in range(n):
    a = input()
    if a[0: 3] == 'не ' or a[0: 3] == 'Не ':
        a = a[3:]
    print(a)
