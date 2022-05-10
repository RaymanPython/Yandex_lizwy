a = []
for i in range(int(input())):
    a.append(int(input()))
p = int(input())
q = int(input())
print(sum(a[p - 1: q]))
