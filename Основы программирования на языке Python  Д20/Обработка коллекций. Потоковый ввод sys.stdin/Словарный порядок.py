def f(x):
    return x.lower()


print(' '.join(sorted(input().split(), key=f)))
