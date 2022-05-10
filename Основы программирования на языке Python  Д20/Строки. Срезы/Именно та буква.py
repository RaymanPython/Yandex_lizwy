a = input()
n = int(input())
s = input()
if (0 < n <= len(a)) and s == a[n - 1] and len(s) == 1:
    print('ДА')
elif (0 < n <= len(a)) and s != a[n - 1] and len(s) == 1:
    print('НЕТ')
else:
    print('ОШИБКА')
