s = input()
n = len(s) // 2
if len(s) % 2 == 1:
    print(' ' * (len(s) // 2) + s[len(s) // 2])
    s = s[0:len(s) // 2] + s[len(s) // 2 + 1:]
    x = ' '
else:
    x = ''
for i in range(n):
    print(' ' * (n - i - 1) + s[n - i - 1] + ' ' * i + x + ' ' * i + s[n + i])
