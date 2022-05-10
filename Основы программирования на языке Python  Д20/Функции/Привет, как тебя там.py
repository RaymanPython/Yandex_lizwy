def who_are_you_and_hello():
    c = True
    while c:
        s = input()
        if s.isalpha():
            if len(s.split()) == 1:
                if s[0] == s[0].upper():
                    if s[1:].lower() == s[1:]:
                        c = False
                        print('Привет, ' + s + '!')
