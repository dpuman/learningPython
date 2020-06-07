class Point:
    default_color = 'Red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_It(self):
        print(f"{self.x} and {self.y}")


point = Point(1, 3)
point.print_It()
print(Point.default_color)
print(point.default_color)


point.z = 4

print(point.z)

another = Point(10, 12)
another.print_It()


Point.default_color = "Yellow"
print(Point.default_color)
print(point.default_color)
print(another.default_color)
