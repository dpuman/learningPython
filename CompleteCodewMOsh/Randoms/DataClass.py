from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


pointOne = Point(1, 2)
pointTwo = Point(1, 2)

print(pointOne == pointTwo)
print(id(pointOne))
print(id(pointTwo))

print(pointOne == pointTwo)

# Dataclass With Nametuple

PointNameTuple = namedtuple("PointNameTuple", ["a", "b"])

p1 = PointNameTuple(a=1, b=2)
p2 = PointNameTuple(a=1, b=2)

print(p1 == p2)
