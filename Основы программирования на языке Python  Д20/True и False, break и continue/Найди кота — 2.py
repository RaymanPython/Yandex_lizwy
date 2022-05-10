a = [input()]
i = 0
while a[i] != 'СТОП':
    a.append(input())
    i += 1
for i in range(len(a)):
    if 'кот' in a[i]:
        print(i + 1)
        break
else:
    print(-1)
