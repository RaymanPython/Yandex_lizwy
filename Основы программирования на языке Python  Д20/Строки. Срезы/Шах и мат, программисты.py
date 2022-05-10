n = int(input())
s = 'ABCDEFGHI'
for i in range(n):
    for j in range(n):
        print(s[j] + str(n - i), end=' ')
    print()
