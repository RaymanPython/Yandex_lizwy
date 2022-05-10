print(' '.join([str(i * i) if (i * i) % 10 != 9 and i % 2 == 1 else '' for i in list(map(int, input().split()))]))
