a = input()
n = int(input())
if n - 1 >= len(a) or n - 1 < 0:
    print('ОШИБКА')
else:
    print(a[n - 1])
