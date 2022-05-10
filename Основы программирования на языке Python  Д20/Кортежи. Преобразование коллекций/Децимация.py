n = int(input())
names = [input() for i in range(n)]
step = int(input())
rounds = int(input())
for j in range(rounds):
    del names[step - 1::step]
print('\n'.join(names))
