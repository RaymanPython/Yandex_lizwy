from sys import stdin

x = 0
for i in stdin.readlines():
    if 'далек' in i.lower():
        x += 1
print(x)
