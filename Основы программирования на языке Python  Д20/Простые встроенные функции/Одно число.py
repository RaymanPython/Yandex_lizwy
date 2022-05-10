x = float(input())
if abs(x) < 1 / 1000000:
    print(1000000)
else:
    print(1 / x)
