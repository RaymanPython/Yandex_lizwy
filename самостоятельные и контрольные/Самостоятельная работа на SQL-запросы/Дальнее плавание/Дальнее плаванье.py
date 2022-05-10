import csv

name = input()
d = int(input())
names = []
with open('far_trip.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        s = row
        if len(s) != 3:
            continue
        if s[0] == name:
            if int(s[-1]) <= d:
                names.append(s[1])
        elif s[1] == name:
            if int(s[-1]) <= d:
                names.append(s[0])
for i in names:
    print(i)
