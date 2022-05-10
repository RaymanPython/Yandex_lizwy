def roots_of_quadratic_equation(a, b, c):
    d = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                return ['all']
            else:
                return []
        else:
            return [-c / b]
    elif d < 0:
        return []
    elif d == 0:
        return [-b / 2 / a]
    else:
        d = d ** 0.5
        return [(-b + d) / 2 / a, (-b - d) / 2 / a]
