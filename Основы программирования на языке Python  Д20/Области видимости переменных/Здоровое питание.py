def diet(a):
    a = a.split(', ')
    x = 0
    for i in a:
        if i in food['диетическое']:
            x += 1
    if float(x) >= len(a) / 2:
        return 'Так держать, Воин Дракона!'
    else:
        return 'Не ешь столько, По!'


food = {
    'жирное': ["растительное масло", 'гамбургер'],
    'сладкое': ['печенье', 'чай', 'мёд', 'сахар', 'торт'],
    'мучное': ["печенье"],
    'диетическое': ['творог', 'фрукты', 'каша', 'зелень', 'овощи', 'рис'],
}
