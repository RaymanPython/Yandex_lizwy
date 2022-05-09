from sys import stdin

x = 0
for i in stdin.readlines():
    s = ' ' + i.lower()
    if ' далек' in s:
        x += 1
print(x)
