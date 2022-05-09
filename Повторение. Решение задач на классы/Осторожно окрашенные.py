class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __str__(self):
        return f'{self.name}{self.x, self.y}'


class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        self.name = name
        self.x = x
        self.y = y
        self.rgb = rgb

    def get_color(self):
        return f'{self.rgb}'

    def __invert__(self):
        res = (255 - self.rgb[0], 255 - self.rgb[1], 255 - self.rgb[2])
        return ColoredPoint(self.name, self.y, self.x, res)
