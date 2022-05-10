def number_to_words(n):
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    k = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    n1 = n - n % 10
    n2 = n % 10
    if (n < 10):
        return f.get(n)
    elif (n >= 10 and n2 == 0):
        return k.get(n)
    elif n > 10 and n < 20:
        return s.get(n)
    elif (n > 20):
        return k.get(n1) + ' ' + f.get(n2)
    else:
        return 'Введено число, которое не лежит в [1:99]!'
