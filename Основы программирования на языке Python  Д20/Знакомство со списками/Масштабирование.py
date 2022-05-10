x = int(input())
y = int(input())
a = []
for i in range(x):
    s = input()
    if i % 2 == 0:
        k = ''
        for j in range(y):
            if j % 2 == 0:
                k += s[j]
        a.append(k)
for i in a:
    print(i)
