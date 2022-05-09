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

    def __eq__(self, other):
        if self.name == other.name and \
                self.x == other.x and \
                self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.name != other.name:
            return True
        else:
            if self.x != other.x:
                return True
            else:
                if self.y != other.y:
                    return True
        return False

    def __lt__(self, other):
        if self.__eq__(other):
            return False
        if self.name < other.name:
            return True
        elif self.name == other.name:
            if self.x < other.x:
                return True
            elif self.x == other.x:
                if self.y < other.y:
                    return True
        return False

    def __gt__(self, other):
        if self.__eq__(other):
            return False
        if self.name > other.name:
            return True
        elif self.name == other.name:
            if self.x > other.x:
                return True
            elif self.x == other.x:
                if self.y > other.y:
                    return True
        return False

    def __ge__(self, other):
        if self.__eq__(other):
            return True
        if self.name > other.name:
            return True
        elif self.name == other.name:
            if self.x > other.x:
                return True
            elif self.x == other.x:
                if self.y > other.y:
                    return True
        return False

    def __le__(self, other):
        if self.__eq__(other):
            return True
        if self.name < other.name:
            return True
        elif self.name == other.name:
            if self.x < other.x:
                return True
            elif self.x == other.x:
                if self.y < other.y:
                    return True
        return False

    def __str__(self):
        return '{0}({1}, {2})'.format(self.name, self.x, self.y)
