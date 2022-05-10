x = input()
s = 0
m = 200
mi = 0
while x != '!':
    x = int(x)
    if 150 <= x <= 190:
        if x < m:
            m = x
        if x > mi:
            mi = x
        s += 1
    x = input()
print(s)
print(m, mi)
