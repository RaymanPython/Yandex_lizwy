n = int(input())
d = 9
i = 1
k = 0
while i * d < n:
    n -= d * i
    i += 1
    d = 10 * d
if i - 1:
    k = int('9' * (i - 1))
print(n // i + k)
