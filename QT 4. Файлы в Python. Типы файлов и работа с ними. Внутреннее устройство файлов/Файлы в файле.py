f = open('input.txt')
a = dict()
b = dict()
c = {'B': 0, 'KB': 10, 'MB': 20, 'GB': 30, 'TB': 40}
for i in f:
    name, x, typex = i.split()
    name, name_type = name.split('.')
    x = int(x)
    a[name_type] = a.get(name_type, []) + [name]
    x *= 2 ** c[typex]
    b[name_type] = b.get(name_type, 0) + int(x)
f.close()
f = open('output.txt', 'w')
for i in sorted(a):
    names = sorted(a[i])
    for j in names:
        print(j + '.' + i, file=f)
    print('----------', file=f)
    s = b[i]
    for type_name in ['TB', 'GB', 'MB', 'KB', 'B']:
        if 2 ** c[type_name] <= s:
            break
    s /= 2 ** c[type_name]
    print('Summary:', int(round(s, 0)), type_name, file=f)
    print(file=f)
f.close()
