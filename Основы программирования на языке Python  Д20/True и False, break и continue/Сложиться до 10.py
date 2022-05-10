s = 0
x = int(input())
i = 1
while x != 0:
    s += x
    if s != 10:
        i += 1
    else:
        break
    x = int(input())
print(i)
