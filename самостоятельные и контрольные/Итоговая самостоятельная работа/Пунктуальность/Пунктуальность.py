import json
import csv

answers = dict()

with open(input(), newline='') as File:
    reader = csv.DictReader(File, delimiter=';')
    for row in reader:
        answers[row['hours']] = answers.get(row['hours'], []) + [row['case']]
for i in answers:
    answers[i] = sorted(answers[i])
with open('accuracy.json', 'w') as cat_file:
    json.dump(answers, cat_file)
