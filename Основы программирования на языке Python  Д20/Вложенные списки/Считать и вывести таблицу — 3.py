n, m = int(input()), int(input())
a = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(input())
    a.append(line)
for i in a:
    print('\t'.join(i))
