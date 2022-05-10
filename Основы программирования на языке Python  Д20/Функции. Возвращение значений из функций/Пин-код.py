def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n and n > 1


def is_palindrom(string):
    return str(string) == str(string)[::-1]


def is_2_pow(n):
    return bin(n).count('1') == 1


def check_pin(str):
    x = [int(i) for i in str.split('-')]
    return 'Корректен' if (IsPrime(x[0]) and is_palindrom(x[1]) and is_2_pow(x[2])) else 'Некорректен'
