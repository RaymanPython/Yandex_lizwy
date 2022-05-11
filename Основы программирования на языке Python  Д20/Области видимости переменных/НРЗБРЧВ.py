gl = 'аАОЭИЮЯЕЁУоэиюяеуёыaeouiyYEAOIU'
zn = '.,!?:;"-'
a = ['"', '"']
translated_text = None


def translate(text):
    global translated_text
    if len(text) == 0:
        translated_text = ''
        return translated_text
    b.append(text)
    tr = []
    txt = []
    r = []
    c = ''
    for i in range(len(b)):
        n = list(b[i])
        for j in range(len(n)):
            if n[j] not in gl and n[j] not in zn:
                r.append(n[j])
        for k in range(len(r)):
            c = c + r[k]
        tr.append(c)
    txt = tr[0].split()
    translated_text = ' '.join(txt)


b = []
