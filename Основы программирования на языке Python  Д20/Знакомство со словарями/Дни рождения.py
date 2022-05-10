dayB = {
    'янв': [],
    'фев': [],
    'мар': [],
    'апр': [],
    'май': [],
    'июн': [],
    'июл': [],
    'авг': [],
    'сен': [],
    'окт': [],
    'ноя': [],
    'дек': [],
}
for i in range(int(input())):
    about = input().split()
    name = about[0]
    month = about[2]
    dayB[month].append(name)
    dayB[month].sort()
for j in range(int(input())):
    inputm = input()
    print(' '.join(dayB[inputm]))
