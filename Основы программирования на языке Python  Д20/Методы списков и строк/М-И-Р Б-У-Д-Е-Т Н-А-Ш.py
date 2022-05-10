res = ''
a = input().split()
for i in a:
    s = ''
    for j in i:
        s += j.upper() + '-'
    s = s[:-1]
    res += s + ' '
print(res)
