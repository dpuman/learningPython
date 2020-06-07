class Point:
    default_color = 'Red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(12, 0)

    def print_It(self):
        print(f"{self.x} and {self.y}")


point = Point.zero()

point.print_It()
