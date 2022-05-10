a = int(input())
b = int(input())
s = input()
for i in range(a):
    if i == 0 or i == a - 1:
        print(s * b)
    else:
        print(s + ' ' * (b - 2) + s)
