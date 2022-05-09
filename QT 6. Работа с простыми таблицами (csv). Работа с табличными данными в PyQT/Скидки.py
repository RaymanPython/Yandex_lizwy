import csv

with open('wares.csv') as x:
    r = csv.DictReader(x, delimiter=";")
    for i in r:
        s1 = int(i['Old price'])
        s2 = int(i['New price'])
        if s1 <= s2:
            pass
        else:
            print(f'{i["Name"]}')
