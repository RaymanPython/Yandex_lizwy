import datetime

import schedule

i = 1


def job():
    global i
    i += 1
    n = int(str(datetime.datetime.now()).split(':')[-3].split()[-1]) % 12 + 1
    print('Ку' * n)


schedule.every(3600).seconds.do(job)
while True:
    if int(str(datetime.datetime.now()).split(':')[-2]) == 0:
        break
while True:
    schedule.run_pending()
