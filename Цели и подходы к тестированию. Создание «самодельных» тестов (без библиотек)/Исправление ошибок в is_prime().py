def is_prime(n):
    if n <= 1:
        return False
    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


if is_prime(int(input())):
    print('YES')
else:
    print('NO')
