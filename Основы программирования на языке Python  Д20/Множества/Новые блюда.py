a = set()
for i in range(int(input())):
    a.add(input())
b = set()
for i in range(int(input())):
    for j in range(int(input())):
        b.add(input())
for i in a:
    if i not in b:
        print(i)
