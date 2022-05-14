import random

n = 500000
k = 0.0
for i in range(n):
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0)
print(4 * k / n)
