s = input()
x = 0
y = 0
m = 0
c = True
k = False
for i in range(len(s)):
    if s[i] == 'о':
        if c:
            x = i
            c = False
            k = True
        y = i
    else:
        if y - x + 1 > m:
            m = y - x + 1
        c = True
if y - x + 1 > m:
    m = y - x + 1
if k:
    print(m)
else:
    print(0)
