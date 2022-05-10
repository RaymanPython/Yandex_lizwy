n = int(input())
for i in range(2, n):
    c = True
    k = 2
    while k < i and c:
        if i % k == 0:
            c = False
        k += 1
    if c:
        print(i)
