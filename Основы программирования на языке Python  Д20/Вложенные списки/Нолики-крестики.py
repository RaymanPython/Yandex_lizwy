n = int(input())
lst_string = []
for i in range(n):
    lst_string.append(input())
for i in lst_string:
    if 'xxx' in i:
        print('x')
        break
    if 'ooo' in i:
        print('o')
        break
else:
    for x in range(n):
        s = ''
        for c in lst_string:
            s += c[x]
        if 'xxx' in s:
            print('x')
            break
        if 'ooo' in s:
            print('o')
            break
    else:
        print('-')
