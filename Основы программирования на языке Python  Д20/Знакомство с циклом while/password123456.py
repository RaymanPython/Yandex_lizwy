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
if len(a) < 8:
    print('Короткий!')
elif not f(a):
    print('Простой!')
else:
    b = input()
    if a != b:
        print('Различаются.')
    else:
        print('OK')
