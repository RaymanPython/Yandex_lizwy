from sys import stdin

x = 0
s = 'далек	далеки далека	далеков далеку	далекам далека	далеков далеком далеками далеке далеках'
a = s.split()
for i in stdin.readlines():
    s = ' ' + i.strip().lower() + ' '
    for j in a:
        if (' ' + j + ' ') in s:
            x += 1
            break
print(x)
