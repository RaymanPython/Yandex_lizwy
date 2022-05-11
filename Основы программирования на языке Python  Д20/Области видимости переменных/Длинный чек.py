def add_item(item_name, item_cost):
    global a
    a.append([item_name, item_cost])


def print_receipt():
    global k, a
    if len(a) > 0:
        print('Чек ' + str(k) + '. Всего предметов: ' + str(len(a)))
        s = 0
        for i in a:
            print(i[0], '-', i[1])
            s += i[1]
        print('Итого:', s)
        k += 1
        a = []
        print('-----')


a = []
k = 1
