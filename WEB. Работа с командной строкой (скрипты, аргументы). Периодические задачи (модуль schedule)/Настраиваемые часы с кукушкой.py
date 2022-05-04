from datetime import datetime
import schedule

sp = list(range(12))
s = input('сьтрока вывода?: ')
lim = input('Время, когда программа неактивна: ')
l1, l2 = lim.split('-')
st = sp[sp.index(int(l1)):sp.index(int(l2)) + 1]


def job():
    flag = True
    t = datetime.now().time()
    h = str(t).split(':')[0]
    m = str(t).split(':')[1]
    if int(m) == 0:
        h = int(h)
        if h >= 12:
            h -= 12
        if h in st:
            c = False
        if c:
            print(int(h) * s)


schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
