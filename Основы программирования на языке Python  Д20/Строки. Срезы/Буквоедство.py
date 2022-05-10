def f(a):
    print(a)
    if len(a) > 2:
        f(a[1:-1])


f(input())
