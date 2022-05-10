n = int(input())
inp = []
ok = []
for i in range(n):
    new_ = input()
    new_spl = new_.split()
    if new_spl[1] in ('4', '5'):
        ok.append(new_)
    inp.append(new_)
print('\n'.join(inp))
print()
print('\n'.join(ok))
