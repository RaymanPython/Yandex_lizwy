def partial_sums(*a):
    b = [0]
    for i in range(len(a)):
        b.append(b[i] + a[i])
    return b
