s1, s2 = set(), set()
t = input()
while t:
    s1.add(int(t))
    t = input()
t = input()
while t:
    s2.add(int(t))
    t = input()
s3 = s1.intersection(s2)
if s3:
    print(*s3, sep='\n')
else:
    print('EMPTY')
