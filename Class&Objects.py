import math

class Circle(object):
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        return math.pi * self.radius**2

circ = Circle(5)
print(circ.radius)
print(circ.area())


class Rectabgle:
    def __init__(self, length, width):
        self.length = length
        self.width = width  

    def area(self):
        return self.length * self.width

circ = Rectabgle(5, 10)
print(circ.length)
print(circ.width)
print(circ.area())
