x = int(input())
s = -1
s1 = -1
while x != 0:
    y = int(input())
    if x < y and s == -1:
        print(y)
        s = y
    if x > y and s != -1 and s1 == -1:
        print(y)
        s1 = y
print(s - s1)
# не решена
