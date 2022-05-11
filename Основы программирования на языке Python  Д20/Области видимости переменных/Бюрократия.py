Name = ''
Vac = ''


def setup_profile(name, vac):
    global Name, Vac
    Name = name
    Vac = vac
    return None


def print_application_for_leave():
    global Name, Vac
    print('Заявление на отпуск в период ', Vac, '. ', Name, sep='')
    return None


def print_holiday_money_claim(amo):
    global Name
    print('Прошу выплатить ', amo, ' отпускных денег. ', Name, sep='')
    return None


def print_attorney_letter(to):
    global Name, Vac
    print('На время отпуска в период ', Vac, sep='', end='')
    print(' моим заместителем назначается ', to, '. ', Name, sep='')
