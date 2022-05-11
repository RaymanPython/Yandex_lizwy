gv = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
      (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
      (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def atr(n):
    if n <= 0:
        return ''
    res = ''
    for i, j in gv:
        while n >= i:
            res += j
            n -= i
    return res


def roman():
    global one
    global two
    global three
    three = one + two
    print('{} + {} = {}'.format(atr(one), atr(two), atr(three)))
