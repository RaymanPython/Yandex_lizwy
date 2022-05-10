def f(n):
    if n != 0:
        a = input() + ' ' + input()
        f(n - 1)
        print(a)


f(int(input()))
