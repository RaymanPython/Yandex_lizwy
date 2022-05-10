a = []
for i in range(int(input())):
    a.append(input())
s = input()
for i in a:
    if s in i:
        print(i)
