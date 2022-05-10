a = input()
ma = ''
mi = '888888888888888888888888888888888888888888888888888888888888888888888888888888888888'
while a != "стоп":
    if len(a) < len(mi):
        mi = a
    if len(a) > len(ma):
        ma = a
    a = input()
if set(ma).issuperset(set(mi)):
    print("ДА")
else:
    print("НЕТ")
