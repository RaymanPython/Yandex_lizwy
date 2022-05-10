s = ''
for _ in range(int(input())):
    x = input()
    if 'лук' not in x:
        s += x + ', '
s = s[:-2]
print(s)
