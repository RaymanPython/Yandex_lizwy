s = 0
n = int(input())
for i in range(n // 2):
    s += int(input())
    s -= int(input())
for i in range(n % 2):
    s += int(input())
print(s)
