def f(a):
    return a[0].upper() + a[1:].lower()


a = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
     "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
     "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
     "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
     "б": "b", "ю": "ju", "ё": "jo"
     }
b = dict()
for i in a.keys():
    b[i.upper()] = f(a[i])
f = open('cyrillic.txt', 'r')
fprint = open('transliteration.txt', 'w')
data = f.read()
lines = data.split('\n')
for i in lines:
    s = ''
    for j in i:
        s += a.get(j, b.get(j, j))
    print(s, file=fprint)
