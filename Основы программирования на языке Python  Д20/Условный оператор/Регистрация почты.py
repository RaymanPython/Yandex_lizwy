n = input()
e = input()
if '@' in list(e) and '@' not in list(n):
    print('OK')
else:
    if '@' in list(n):
        print("Некорректный логин")
    else:
        print('Некорректный адрес')
