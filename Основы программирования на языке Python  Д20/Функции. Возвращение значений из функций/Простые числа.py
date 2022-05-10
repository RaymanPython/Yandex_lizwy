def prime(n):
    c = True
    i = 2
    while c and i * i <= n:
        if n % i == 0:
            c = False
        i += 1
    if c:
        return 'Простое число'
    else:
        return 'Составное число'
