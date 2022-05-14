a = input().split(' ')
for t, i in enumerate(a):
    a[t] = int(i)


def solve(a):
    if len(a) == 3:
        d = a[1] ** 2 - 4 * a[0] * a[2]
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            x = ["all"]
        elif a[0] == 0 and a[1] == 0:
            x = ''
        elif a[0] == 0:
            x = [-a[2] / a[1]]
        elif a[1] == 0:
            x = [(a[2] // a[0]) ** 0.5]
        elif a[2] == 0:
            x = [0, -a[1] // a[0]]
        else:
            if d == 0:
                x = [-a[1] // (2 * a[0])]
            elif d < 0:
                x = ''
            else:
                x = [int((-a[1] + d ** 0.5) // (2 * a[0])),
                     int((-a[1] - d ** 0.5) // (2 * a[0]))]
        return x
    elif len(a) == 2:
        return [-a[1] / a[0]]
    elif len(a) == 1:
        if a[0] == 0:
            return ["all"]
        else:
            return []
    else:
        return ["all"]


print(*sorted(solve(a)))
