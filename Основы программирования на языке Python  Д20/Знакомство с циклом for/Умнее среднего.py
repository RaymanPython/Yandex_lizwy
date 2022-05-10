n = int(input())
s = int(input())
print('0')
for i in range(1, n):
    x = int(input())
    if x < s / i:
        print('<')
    elif x > s / i:
        print('>')
    else:
        print('0')
    s += x
