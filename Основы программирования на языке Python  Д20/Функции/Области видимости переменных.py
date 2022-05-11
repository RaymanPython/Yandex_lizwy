def circle_length(r):
    return 2 * 3.14159 * r


def circle_area(r):
    return 3.14159 * r * r


def main():
    r = float(input())
    print(circle_length(r), circle_area(r))
