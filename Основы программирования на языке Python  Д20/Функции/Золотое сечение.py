def golden_ratio(i):
    if i < 2:
        a, b = 1, 1
    else:
        a = 1
        b = 1
        for j in range(i - 1):
            a, b = b, a + b
    print(b / a)
