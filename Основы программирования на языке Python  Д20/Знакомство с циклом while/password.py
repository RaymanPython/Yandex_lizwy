def fa():
    def f(a):
        i = 0
        c = True
        while i <= len(a) - 3 and c:
            if a[i] == '1' and a[i + 1] == '2' and a[i + 2] == '3':
                return False
                c = False
            i += 1
        if c:
            return True

    a = input()
    b = input()
    if len(a) < 8:
        print('Короткий!')
        fa()
    elif not f(a):
        print('Простой!')
        fa()
    else:
        if a != b:
            print('Различаются.')
            fa()
        else:
            print('OK')


fa()
