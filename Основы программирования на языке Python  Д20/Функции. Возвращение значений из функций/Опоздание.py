def late(start, end, arr):
    run = 5
    go = 15
    arr = arr[::-1]
    minute_start = get_minute(start)
    minute_end = get_minute(end)
    dt = minute_end - minute_start
    if dt < 20:
        return 'Опоздание'
    for item in arr:
        if (item <= (dt - go)) > 0:
            if item - run > 0:
                return 'Выйти через ' + str(item - run) + ' минут'
            else:
                return 'Опоздание'
    return 'Опоздание'


def get_minute(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)
