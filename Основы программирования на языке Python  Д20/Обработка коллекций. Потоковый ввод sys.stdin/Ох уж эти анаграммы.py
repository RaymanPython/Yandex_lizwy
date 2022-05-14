a = {}
for i in range(int(input())):
    x = input().lower()
    s = ''.join(sorted(x))
    a[s] = a.get(s, set())
    a[s].add(x)
s = [' '.join(sorted(i)) for i in a.values() if len(i) > 1]
print('\n'.join(sorted(s)))
