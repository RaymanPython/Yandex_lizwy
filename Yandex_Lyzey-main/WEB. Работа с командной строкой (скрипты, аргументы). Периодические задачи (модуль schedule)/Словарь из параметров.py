import sys

try:
    a = list(map(str, sys.argv[1:]))
    if len(a) == 0:
        pass
    else:
        res = dict()
        flag = False
        for i in range(len(a)):
            if a[i] == '--sort':
                flag = True
                continue
            x, y = a[i].split('=')
            res[x] = y
        if flag:
            ans = sorted(list(res.keys()))
        else:
            ans = list(res.keys())
        for i in ans:
            print(f'Key: {i} Value: {res[i]}')
except ValueError:
    print('ValueError')
