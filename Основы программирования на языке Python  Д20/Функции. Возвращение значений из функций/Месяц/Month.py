def month_name(n, e):
    if e == 'en':
        a = 'January, February, March, April, May, June, July,'
        a += ' August, September, October, November, December'
        a = a.split(', ')
        return a[n - 1]
    else:
        a = 'Январь. Февраль. март. Апрель. Май. Июнь. '
        a += 'Июль. Август. Сентябрь. Октябрь. Ноябрь. Декабрь'
        a = a.split('. ')
        return a[n - 1].lower()
