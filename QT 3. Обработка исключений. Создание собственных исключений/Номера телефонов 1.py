s = input()
res = 'error'
s = ''.join(s.split())
if (len(s) >= 12 and s[0] + s[1] == '+7') or (len(s) >= 11 and s[0] == '8'):
    res1 = '+7'
    IndexNum = 1
    SR = 0
    SL = 0
    k = 0
    if s[0] == '+':
        IndexNum += 1
    for i in range(IndexNum, len(s)):
        if s[i] != '-':
            k = 0
        if s[i] == '-':
            k += 1
            if k > 1:
                res1 = ''
                break
            if i == len(s) - 1:
                res1 = ''
                break
        elif s[i] == '(':
            SL += 1
        elif s[i] == ')':
            SR += 1
        elif s[i] in '0123456789':
            res1 += s[i]
        else:
            res1 = ''
            break
        if SL < SR:
            break
    if len(res1) == 12 and SL == SR and SL < 2:
        res = res1
print(res)
