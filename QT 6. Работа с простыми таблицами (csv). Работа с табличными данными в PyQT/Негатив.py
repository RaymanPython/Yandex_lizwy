with open('input.bmp', 'rb') as f:
    data = list(bytes(f.read()))
    a = []
    for i, j in enumerate(data):
        if i < 54:
            a.append(j)
        else:
            a.append(255 - j)
with open('res.bmp', 'wb') as f:
    f.write(bytes(a))
