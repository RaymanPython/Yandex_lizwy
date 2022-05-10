n = input()
s = []
s1 = []
b = 0
a, it = int(n[:4]), int(n[4:])
for i in range(a):
    a = input()
    price, k, summ = int(a[0:7]), int(a[8:12]), int(a[13:18])
    if price * k != summ:
        s.append(i + 1)
    summ1 = k * price
    s1.append(summ1)
for i in s1:
    b += i
print(it - b)
for i in s:
    print(i, end=' ')
