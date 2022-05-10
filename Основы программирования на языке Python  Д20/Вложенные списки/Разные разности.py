a = []
s = set()
for i in range(int(input())):
    a.append(int(input()))
for i in range(len(a)):
    for j in range(i + 1):
        s.add(a[i] - a[j])
        s.add(a[j] - a[i])
s = list(s)
s.sort()
for i in s:
    print(i)
