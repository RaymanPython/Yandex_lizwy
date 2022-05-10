a = list(map(int, list(input())))
s = a[0] + a[1]
s1 = a[1] + a[2]
if s > s1:
    print(str(s) + str(s1))
else:
    print(str(s1) + str(s))
