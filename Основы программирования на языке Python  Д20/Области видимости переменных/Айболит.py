def hello(name):
    print('Здравствуйте, {}! Вашу карту ищут...'.format(name))


def search_card(name):
    global base
    for i, val in enumerate(base):
        if val == name:
            print('Ваша карта с номером {} найдена'.format(i + 1))
            return
    print('Ваша карта не найдена')


base = ["Иван", "Юлия Иванкова"]
