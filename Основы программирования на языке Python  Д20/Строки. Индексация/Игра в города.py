a = input()[-1]
x = input()
while x[0] == a:
    a = x[-1]
    x = input()
print(x)
