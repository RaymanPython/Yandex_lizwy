m = [input() for _ in range(int(input()))]
print(*(str(m.index(i) + 1) + " " + str(i.find('кот') + 1) for i in m if 'кот' in i), sep="\n")
