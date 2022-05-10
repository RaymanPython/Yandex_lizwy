a = int(input())
b = int(input())
for i in range(a):
    line = [input() for ш in range(b)]
    if i != 0 and i != a - 1:
        print('\t'.join(line))
    else:
        print('\t'.join(line))
