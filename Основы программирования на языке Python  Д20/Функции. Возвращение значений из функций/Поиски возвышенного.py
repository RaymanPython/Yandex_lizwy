def find_mountain(a):
    x, y = -1, -1
    m = -1
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > m:
                m = a[i][j]
                x, y = j, i
    return y, x
