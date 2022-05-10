n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i * j, end="\t")
        j += 1
    i += 1
    print()
