a = input()
b = input()
if a == 'камень' and b == 'ножницы':
    print('первый')
elif a == 'ножницы' and b == 'бумага':
    print('первый')
elif a == 'бумага' and b == 'камень':
    print('первый')
elif a == b:
    print('ничья')
elif a == 'пират' and b == 'пират':
    print('ничья')
elif a == 'ром' and b == 'пират':
    print('первый')
elif a == 'пират' and b == 'ножницы':
    print('первый')
elif a == 'ром' and b == 'бумага':
    print('первый')
elif a == 'камень' and b == 'ром':
    print('первый')
elif a == 'ножницы' and b == 'ром':
    print('первый')
elif a == 'бумага' and b == 'пират':
    print('первый')
elif a == 'пират' and b == 'камень':
    print('первый')
else:
    print('второй')
