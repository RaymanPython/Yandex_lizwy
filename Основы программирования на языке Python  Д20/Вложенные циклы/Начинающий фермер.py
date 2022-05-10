x = int(input())
s = int(input())
for b in range(1, min(s, x // 20) + 1):
    for k in range(0, min(s, x // 10) + 1):
        for t in range(0, min(s, x // 5) + 1):
            if b * 20 + k * 10 + t * 5 == x:
                if b + k + t == s:
                    print(b, k, t)
