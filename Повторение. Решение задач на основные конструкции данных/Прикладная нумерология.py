def f(x):
    return '0' * (2 - len(str(x))) + str(x)


a = list(map(int, input().split()))
a.sort()
a1 = list(map(lambda x: sum(map(int, list(str(x)))), a))
b = list(map(int, input().split()))
b.sort()
b1 = list(map(lambda x: sum(map(int, list(str(x)))), b))
for i in range(len(a)):
    for j in range(len(b)):
        if a1[i] != b1[j]:
            print(f(a[i]) + ':' + f(b[j]))
