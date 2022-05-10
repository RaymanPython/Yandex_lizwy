city = input()
town = input()
if city[-1] == town[0]:
    print('ВЕРНО')
elif city[-1] == 'ь':
    if city[-2] == town[0]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')
else:
    print('НЕВЕРНО')
