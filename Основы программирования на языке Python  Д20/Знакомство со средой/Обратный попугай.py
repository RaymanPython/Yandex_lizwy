def f(x, i):
    if i > 0:
        f(input(), i - 1)
    print(x)


f(input(), 2)
