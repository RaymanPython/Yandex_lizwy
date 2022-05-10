n = int(input())
for i in range(n):
    a = input()
    if a[0:2] == '%%':
        a = a[2: len(a)]
    elif a[0: 4] == '####':
        continue
    print(a)
