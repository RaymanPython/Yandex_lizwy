x = int(input())
i = 0
while x % 2 == 0 and x > 1:
    x //= 2
    i += 1
if x == 1:
    print(i)
else:
    print('НЕТ')
