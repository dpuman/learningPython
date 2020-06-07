class Point:
    def draw(self):
        print("Draw of Point")


point = Point()
print(type(point))
point.draw()
print(isinstance(point, Point))
