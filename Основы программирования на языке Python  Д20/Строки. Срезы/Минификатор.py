n = int(input())
mark = False
slash = False
char = 0
result = []
for i in range(n):
    a = input()
    while a[char] == " ":
        result.append(" ")
        char += 1
    for i2 in range(char, len(a)):
        if not slash:
            if a[i2] == "'":
                result.append(a[i2])
                mark = not mark
            elif a[i2] == "\\":
                result.append(a[i2])
                slash = True
            elif a[i2] == "#":
                if mark:
                    result.append(a[i2])
                else:
                    break
            elif a[i2] == " ":
                if mark:
                    result.append(a[i2])
                else:
                    if i2 + 1 != len(a):
                        if a[i2 + 1] == " ":
                            result.append("")
                        else:
                            result.append(a[i2])
            else:
                result.append(a[i2])
        else:
            slash = False
            result.append(a[i2])
    print(''.join(result))
    result = []
    mark = False
    slash = False
    char = 0
