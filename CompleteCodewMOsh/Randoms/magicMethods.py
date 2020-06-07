class Point:
    default_color = 'Red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}and{self.y} "

    def print_It(self):
        print(f"{self.x} and {self.y}")


point = Point(10, 23)
print(str(point))
