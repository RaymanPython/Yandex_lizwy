rows = int(input())
cols = int(input())
for i in range(rows):
    col = [input() for _ in range(cols)]
    if (i != 0) and (i != rows - 1):
        print('\t'.join(sorted(col)))
    else:
        print('\t'.join(col))
