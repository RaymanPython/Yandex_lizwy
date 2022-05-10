c = True
a = 'Кот'
b = 'кот'
for i in range(int(input())):
    s = input()
    if s.find(a, 0, len(s)) == -1 and s.find(b, 0, len(s)) == -1:
        p = 0
    else:
        if c:
            c = False
            print('МЯУ')
if c:
    print('НЕТ')
