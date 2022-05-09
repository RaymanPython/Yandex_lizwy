from sys import stdin

z = []
main_word = input()
s = [i.replace('\n', '') for i in stdin.readlines()]
for i in s:
    pr = []
    a = (list(main_word)).copy()
    for j in list(i):
        if j in a:
            del a[a.index(j)]
            pr.append(True)
        else:
            pr.append(False)
    if False not in pr:
        z.append(i)
print(len(z))
for i in z:
    print(i)
