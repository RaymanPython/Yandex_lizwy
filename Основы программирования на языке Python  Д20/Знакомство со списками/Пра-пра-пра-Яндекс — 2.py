a = []
for i in range(int(input())):
    a.append(input())
s = []
for i in range(int(input())):
    s.append(input())
for i in a:
    c = True
    for j in s:
        if j not in i:
            c = False
            break
    if c:
        print(i)
