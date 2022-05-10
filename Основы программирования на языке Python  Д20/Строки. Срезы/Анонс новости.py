m = int(input())
n = int(input())
for i in range(n):
    a = input()
    if len(a) > m:
        a = a[0: m - 3] + '...'
    print(a)
