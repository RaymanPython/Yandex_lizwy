a = list(map(int, input().split()))
s = input().split()
res = ''
for i in a:
    res += s[i - 1].lower() + ' '
res = res[0].upper() + res[1:]
print(res)
