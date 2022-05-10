import json
import csv
import requests
import sys

answers = []
address = sys.argv[1]
port = sys.argv[2]
response = requests.get(f'http://{address}:{port}').json()
abc = 'a'
lenght = 0
keys = []
i = 3
while i < len(sys.argv):
    if sys.argv[i] != '-':
        keys.append(sys.argv[i])
    elif sys.argv[i] == '-abc':
        abc = sys.argv[i + 1]
        i += 1
    elif sys.argv[i] == '-length':
        length = int(sys.argv[i + 1])
    i += 1
for i in response:
    s = response[i]
    min_length = 100000000
    max_length = 0
    summ = 0
    n1 = 0
    for j in s:
        if i in keys:
            if len(j) > lenght and j > abc:
                min_length = min(min_length, len(j))
                max_length = max(max_length, len(j))
                summ += len(j)
                n1 += 1
        else:
            min_length = min(min_length, len(j))
            max_length = max(max_length, len(j))
            summ += len(j)
            n1 += 1
    if n1 == 0:
        n1 = 1
    pr = {
        "object": i,
        "min_length": min_length,
        "max_length": max_length,
        "average": round(summ / n1)
    }
    answers.append(pr)
answers = sorted(answers, key=lambda x: x['object'])
with open('sounds.json', 'w') as cat_file:
    json.dump(answers, cat_file)
