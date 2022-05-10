x = int(input())
n = 0
while x != 1:
    n += 1
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
print(n)
