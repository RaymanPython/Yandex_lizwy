print(sum(list(map(list(filter(list(range(10, 100)), lambda x: x % 9 == 0)), lambda x: x ** 2))))
