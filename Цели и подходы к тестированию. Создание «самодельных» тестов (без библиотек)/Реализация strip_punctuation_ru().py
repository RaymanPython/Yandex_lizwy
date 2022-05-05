def strip_punctuation_ru(data):
    p = [',', '.', ':', ';', '!', '?', '"', ' - ']
    for i in p:
        data = ' '.join(data.split(i))
    b = data.split()
    a = []
    for i in b:
        if len(i) != 0:
            a.append(i)
    data = ' '.join(a)
    return data
