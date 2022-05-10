n = 1000
y = n // 2
print(y)
n1 = 0
x = input()
while x != '=':
    if x == '<':
        n = y - 1
    else:
        n1 = y + 1
    y = n1 + (n - n1) // 2
    print(y)
    x = input()
