def print_long_words(text):
    text = text.lower()
    k = ''
    for i in text:
        if i.isalpha():
            k += i
        else:
            x = 0
            for j in k:
                if j in 'аоэиуыеёюяaeiouy':
                    x += 1
            if x >= 4:
                print(k)
            k = ''
