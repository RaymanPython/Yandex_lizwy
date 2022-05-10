x = input()
y = input()
z = input()
c = (x == "раз" and y == "два" and z == "три")
if c or (x == "1" and y == "2" and z == "3") or (x == "один" and y == "два" and z == "три"):
    print("ГОРИ")
else:
    print("НЕ ГОРИ")
