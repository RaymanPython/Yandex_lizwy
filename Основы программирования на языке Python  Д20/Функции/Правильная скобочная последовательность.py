def bracket_check(s):
    s = list(s)
    a = [')', '}', ']']
    b = ['(', '{', '[']
    c = []
    res = True
    for i in s:
        if i in b:
            c.append(i)
        elif i in a:
            if i == ')':
                d = 0
            elif i == '}':
                d = 1
            elif i == ']':
                d = 2
            if len(c) > 0:
                if c[-1] == b[d]:
                    c.pop(-1)
                else:
                    res = False
            else:
                res = False
    if len(c) == 0 and res:
        print('YES')
    else:
        print('NO')
