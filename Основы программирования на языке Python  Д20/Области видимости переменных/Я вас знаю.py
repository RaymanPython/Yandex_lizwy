name = ''


def polite_input(txt):
    global name
    if name == '':
        name = input()
        print("Как вас зовут?")
    print(name + ", " + txt)
    return input()
