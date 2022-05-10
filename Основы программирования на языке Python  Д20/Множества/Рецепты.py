a = set()
for _ in range(int(input())):
    a.add(input())
for _ in range(int(input())):
    s = input()
    c = True
    for i in range(int(input())):
        d = input()
        if d not in a:
            c = False
    if c:
        print(s)
