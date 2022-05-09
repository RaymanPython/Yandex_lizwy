s = open('data.txt', 'rb').read()
a = len(s)
print(' ' * 10 + ' '.join(f'{hex(i)[2:]:0>2}' for i in range(16)), '\n')
for i in range(a // 16 + 1):
    s1 = s[i * 16: i * 16 + 16]
    if s1:
        printable = ''.join((chr(p) if chr(p).isprintable() else '.' for p in s1))
        print(('%0.5x0    ' % i) +
              ''.join(('%0.2x ' % p for p in s1)) +
              ' ' * ((16 - len(s1)) * 3 + 4) + printable)
