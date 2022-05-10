a = []
b = []
n = int(input())
for i in range(n):
    x = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            x += 1
    print(x)
    a.append(x)
    b = [x] + b
