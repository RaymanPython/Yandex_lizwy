class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return (self.x)

    def get_y(self):
        return (self.y)

    def get_coords(self):
        return self.x, self.y

    def __invert__(self):
        return Point(self.name, self.y, self.x)
        '''self.x, self.y = self.y, self.x'''
        '''return '{}({}, {})'.format(self.name, self.x, self.y)'''

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __str__(self):
        return '{0}({1}, {2})'.format(self.name, self.x, self.y)
