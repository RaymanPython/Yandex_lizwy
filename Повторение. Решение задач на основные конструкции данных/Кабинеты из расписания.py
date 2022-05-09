import re

ans = {}
with open("input.txt", 'r', encoding='UTF-8') as f:
    for line in f:
        if line == ' ':
            continue
        if re.search("\\d+", line):
            number = int(line.split()[-1])
            val = line[:line.index(str(number))].strip()
            if number not in ans.keys():
                ans[number] = [val]
            elif val not in ans[number]:
                ans[number].append(val)
    for k in sorted(ans.keys()):
        print(f'{k}:', end=' ')
        print(', '.join(ans[k]))
