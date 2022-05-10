def space_game(text):
    x = 0
    for i in text:
        if i == ' ':
            x += 1
    if x % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')
