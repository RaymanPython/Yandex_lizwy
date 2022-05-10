name = input()
ok = True
for i in range(len(name)):
    if name[i] not in 'qwertyuiopasdfghjkzxcvbnml0123456789_' and ok:
        print('Неверный символ:', name[i])
        ok = False
if ok:
    print('OK')
