numbers = [2, 5, 7, 7, 8, 4, 1, 6]
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print('even = {}\nodd = {}'.format(even, odd))
