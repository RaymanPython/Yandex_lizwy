import csv

a = []
s = 1000
with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if int(row[1]) <= s:
            a.append([row[0], int(row[1])])
a.sort(key=lambda x: x[1])
res = []
for i in a:
    if s <= 0:
        break
    if i[1] > s:
        break
    if i[1] == 0:
        k = 10
    else:
        k = s // i[1]
    if k == 0:
        continue
    if k > 10:
        k = 10
    for j in range(k):
        if i[1] <= s:
            res.append(i[0])
            s -= i[1]
        else:
            break
if len(res) > 0:
    print(', '.join(res))
else:
    print('error')
