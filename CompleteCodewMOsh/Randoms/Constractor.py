class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_it(self):
        print(f"{self.x} and {self.y}")


point = Point(1, 2)

point.print_it()
