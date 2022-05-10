n = int(input())
while True:
    if n % 2 == 1:
        a = 1
        n -= a
        print(a, n)
    elif n % 2 != 0:
        a = 3
        n -= a
        print(a, n)
    elif n % 2 != 0 and n < 3:
        a = 1
        n -= a
        print(a, n)
    elif n == 2:
        a = 2
        n = 0
        print(a, n)
    if n == 0:
        print('ИИ выиграл!')
        break
    b = int(input())
    if b > 3 or b < 1:
        print('Некорректный ход:', b)
    else:
        n -= b
        print(b, n)
        if n == 0:
            print('Вы выиграли!')
            break
