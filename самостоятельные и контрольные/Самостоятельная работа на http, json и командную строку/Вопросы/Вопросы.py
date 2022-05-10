import sys
import json

answers = dict()
names = ['beings', 'nature', 'rest']
for i in names:
    answers[i] = dict()
for line in sys.stdin:
    s = line.rstrip()
    if s == '':
        break
    s = s.split(': ')
    n = int(s[0]) - 1
    s = s[1]
    dc = answers[names[n]]
    s = s.split()
    dc[len(s)] = sorted(dc.get(len(s), []) + [s[-1]])[::-1]
    answers[names[n]] = dc

with open('questions.json', 'w') as cat_file:
    json.dump(answers, cat_file)
