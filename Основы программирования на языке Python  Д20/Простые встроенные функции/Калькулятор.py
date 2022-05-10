x = float(input())
y = float(input())
s = input()
if s == '-':
    print(x - y)
elif s == '+':
    print(x + y)
elif s == '/':
    if y == 0:
        print(888888)
    else:
        print(x / y)
elif s == '*':
    print(x * y)
else:
    print(888888)
