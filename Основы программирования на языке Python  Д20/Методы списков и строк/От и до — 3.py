def f(x):
    return x * x


a = list(map(int, input().split()))
n, k = map(int, input().split())
print(sum(map(f, a[n: k + 1])))
