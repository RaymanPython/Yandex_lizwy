def ask_password():
    a = []
    for i in range(3):
        a.append(input())
    if 'password' in a:
        print('Пароль принят')
    else:
        print('В доступе отказано')
