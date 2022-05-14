import random

a = int(random.uniform(1, 50))
b = int(random.uniform(1, 50))
scoring = {'Яблочко': 50, 'Зеленое_кольцо': 25,
           'Внешнее_кольцо': {1: 8, 2: 6, 3: 42, 4: a, 5: a, 6: a, 7: 38, 8: 1,
                              9: 41, 10: 14, 11: 38, 12: 38, 13: 3, 14: 36, 15: 48,
                              16: a, 17: 21, 18: a, 19: 11, 20: 50},
           'Внутреннее_кольцо': {1: 2, 2: 16, 3: 56, 4: b, 5: 16, 6: b, 7: 38,
                                 8: b, 9: b, 10: b, 11: b, 12: b, 13: b, 14: 21,
                                 15: b, 16: b, 17: b, 18: b, 19: b, 20: 39}}


def score(zona, cector=0):
    if cector == 0:
        return scoring[zona]
    else:
        return scoring[zona][cector]
