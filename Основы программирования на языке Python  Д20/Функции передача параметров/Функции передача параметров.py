daily_food = []


def count_food(a):
    s = 0
    for i in a:
        s += daily_food[i - 1]
    return s
