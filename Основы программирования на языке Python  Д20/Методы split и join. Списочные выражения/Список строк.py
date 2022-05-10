a = input().split()
s = '["'
for i in range(len(a)):
    if i != len(a) - 1:
        s += a[i]
        s += '", "'
    else:
        s += a[i]
        s += '"]'
print(s)
