def get_transactions(t):
    if t == 'print_it':
        for i in dcttime:
            print(dcttime[i], i, dctmoney[i])
        return
    where = t[t.find('-') + 1:t.find(':')]
    how_many = int(t[t.find(':') + 1:])
    if where in dcttime:
        dcttime[where] += 1
        dctmoney[where] += how_many
    if where not in dcttime:
        dcttime[where] = 1
        dctmoney[where] = how_many


dcttime = {}
dctmoney = {}
