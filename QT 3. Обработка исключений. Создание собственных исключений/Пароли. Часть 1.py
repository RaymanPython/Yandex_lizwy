def F(a):
    bad_sequence = ['qwertyuiop', 'asdfghjkl',
                    'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    num = list('1234567890')
    if len(a) <= 8:
        return 'error'
    if a.islower() or a.isupper():
        return 'error'
    if a.isdigit() or a.isalpha():
        return 'error'
    b = a.lower()
    for i in bad_sequence:
        for j in range(len(i) - 2):
            if i[j: j + 3] in b:
                return 'error'
    for i in num:
        if i in a:
            return 'ok'
    return 'error'


print(F(input()))
