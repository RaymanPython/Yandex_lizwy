a = int(input())
s = a // 1000
s1 = (a // 100) % 10
s2 = (a // 10) % 10
s3 = a % 10
if s > s1:
    s, s1 = s1, s
if s > s2:
    s, s2 = s2, s
if s > s3:
    s, s3 = s3, s
if s1 > s2:
    s1, s2 = s2, s1
if s1 > s3:
    s1, s3 = s3, s1
if s2 > s3:
    s2, s3 = s3, s2
if s == 0:
    if s1 != 0:
        s, s1 = s1, s
    elif s2 != 0:
        s, s2 = s2, s
    elif s3 != 0:
        s, s3 = s3, s
print(str(s) + str(s1) + str(s2) + str(s3))
