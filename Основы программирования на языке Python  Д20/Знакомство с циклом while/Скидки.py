x = input()
s = 0
while float(x) >= 0:
    x = float(x)
    if x > 1000:
        s += x * 95 / 100
    else:
        s += x
    x = input()
print(s)
