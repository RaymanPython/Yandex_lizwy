for i in range(1, int(input()) + 1):
    x = i
    while i:
        print('Осталось секунд: ' + str(i - 1))
        i -= 1
    print(f'Пуск ' + str(x))
