a = input()
b = input()
by = "бумага"
n = "ножницы"
k = "камень"
if a == b:
    print("ничья")
elif a == by and b == n:
    print("второй")
elif a == by and b == k:
    print("первый")
elif a == n and b == by:
    print("первый")
elif a == n and b == k:
    print("второй")
elif a == k and b == by:
    print("второй")
elif a == k and b == n:
    print("первый")
