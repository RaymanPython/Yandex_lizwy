n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
mi = int(input())
ma = int(input())
for i in a:
    if mi <= i <= ma:
        print(i)
