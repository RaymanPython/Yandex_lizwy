import sys

index1, index2 = 0, 0
slova1, slova2, slova3, p = '', '', '', ''
text = list(map(str.strip, sys.stdin))
text = ' '.join(text)
text = text.replace(',', ' ').replace('  ', ' ')
while index2 < len(text):
    char = text[index2]
    if char == '.':
        slovo = text[index1:index2].lower()
        slova1 += p + slovo + ' '
        p = ''
        index1 = index2 + 1
    elif char == '?':
        slovo = text[index1:index2].lower()
        slova2 += p + slovo + ' '
        p = ''
        index1 = index2 + 1
    elif char == '!':
        slovo = text[index1:index2].lower()
        slova3 += p + slovo + ' '
        p = ''
        index1 = index2 + 1
    else:
        if char == ' ':
            slovo = text[index1:index2].lower()
            index1 = index2 + 1
            p += slovo + ' '
    index2 += 1
slova1 = set(slova1.split())
slova2 = set(slova2.split())
slova3 = set(slova3.split())
slova1.intersection_update(slova2)
slova1.difference_update(slova3)
slova1 = sorted(slova1)
print(*slova1)
