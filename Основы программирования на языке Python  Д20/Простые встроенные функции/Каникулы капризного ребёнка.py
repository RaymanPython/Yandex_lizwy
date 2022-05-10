a = [input(), input()]
if ('Тула' == a[0] or 'Пенза' == a[1]) and len(set(a)) == 2:
    if 'Тула' not in a or 'Пенза' not in a:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')
