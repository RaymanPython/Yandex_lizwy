import datetime as dt

din = dt.datetime.now()
dn = dt.timedelta(days=int(input()))
print((din + dn).day, (din + dn).month)
