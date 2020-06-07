class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point = Point(10, 9)
other = Point(12, 10)

addition = point+other

print(addition.x+addition.y)
print(Point)
