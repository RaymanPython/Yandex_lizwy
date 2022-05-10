s = ''
for i in list(input()):
    s += str(ord(i)) + ', '
print(s[0: -2])
