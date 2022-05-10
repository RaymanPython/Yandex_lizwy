def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
x = int(input())
y = int(input())
for i in range(n - 1):
    x1 = int(input())
    y1 = int(input())
    x = x * y1 + x1 * y
    y = y * y1
d = gcd(x, y)
print(str(x // d) + '/' + str(y // d))
