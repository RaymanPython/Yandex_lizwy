a = list(map(int, list(input())))
if max(a) + min(a) == (sum(a) - max(a) - min(a)) * 2:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
