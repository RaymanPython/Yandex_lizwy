a = input()
k = 1
s = ''
for i in list(a):
    if i != s:
        if s != '':
            print(k, s)
            k = 1
            s = i
        else:
            k = 1
            s = i
    else:
        k += 1
if s != '':
    print(k, s)
