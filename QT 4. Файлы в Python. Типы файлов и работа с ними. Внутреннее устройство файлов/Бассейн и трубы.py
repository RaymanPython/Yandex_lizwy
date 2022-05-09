f = open('pipes.txt', 'r')
f2 = open("time.txt", "w")
s = [line.rstrip() for line in f]
d = []
d1 = []
flag = 0
for i in s:
    if flag == 0:
        if i != '':
            d.append(eval(i))
        else:
            flag += 1
    else:
        s1 = i.split()
        for j in s1:
            d1.append(d[int(j) - 1])
f2.write(str(60 / sum([1 / i for i in d1])))
f2.close()
f.close()
