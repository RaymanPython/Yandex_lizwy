n = int(input())
while n > 0:
    x = int(input())
    if 0 < x and x <= 3 and x <= n:
        n -= x
    print(n)
