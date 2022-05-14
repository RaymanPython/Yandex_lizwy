import sys

s = dict()
b = ord('A')
data = list(map(str.strip, sys.stdin))
for word in data:
    if sum([ord(i) - b + 1 for i in word.upper()]) in list(s.keys()):
        s[sum([ord(i) - b + 1 for i in word.upper()])].append(word)
    else:
        s[sum([ord(i) - b + 1 for i in word.upper()])] = [word]

for h in sorted(list(s.keys())):
    print('\n'.join(sorted(s[h])))
