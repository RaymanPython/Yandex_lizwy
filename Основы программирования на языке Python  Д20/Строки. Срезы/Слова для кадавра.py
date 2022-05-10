s = input()
a = input()
d = False
while a != "":
    converted = ""
    for i in a:
        if i in "ауеыоэяиюё":
            converted += "0"
        else:
            converted += "1"
    c = True
    if s.find("*") != -1:
        s1 = s[:s.find("*")]
        s2 = s[s.find("*") + 1:]
        converted1 = converted[:len(s1)]
        converted2 = converted[
                     len(converted) - len(s2) if len(converted) - len(converted1) >= len(s2)
                     else len(s1) + 1:]
        if len(converted1) == len(s1):
            for n, j in enumerate(converted1):
                if not (s1[n] == "?" or s1[n] == j):
                    c = False
                    break
        else:
            c = False
        if len(converted2) == len(s2):
            for n, j in enumerate(converted2):
                if not (s2[n] == "?" or s2[n] == j):
                    c = False
                    break
        else:
            c = False
    else:
        if len(converted) == len(s):
            for n, j in enumerate(converted):
                if not (s[n] == "?" or s[n] == j):
                    c = False
                    break
        else:
            c = False
    if c:
        print(a)
        d = True
    a = input()
if not d:
    print("Есть нечего, значить!")
