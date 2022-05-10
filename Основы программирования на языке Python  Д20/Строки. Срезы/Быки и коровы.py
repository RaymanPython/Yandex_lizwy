a = input()
b = input()
x, y = 0, 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == j:
                x += 1
            else:
                y += 1
print(x, y)
