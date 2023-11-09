from math import pi

class Cylinder:

    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return circle * 2 + side

    def __init__(self, diametr, high):
        self.diametr = diametr
        self.high = high
        self.area = self.make_area(diametr, high)

    def __str__(self):
        return (f'd = {self.diametr}, h = {self.high}, area = {self.area}')

    def get_info(self):
        return (f'd = {self.diametr}, h = {self.high}, area = {self.area}')

    def __eq__(self, other):
        return self.diametr == other.diametr and self.high == other.high

    def __add__(self, other):
        self.diametr = self.diametr + other.diametr
        self.high = self.high + other.high
        return Cylinder(self.diametr, self.high)

c = Cylinder(4, 2)
c1 = Cylinder(2, 4)
print(c)
print(c.get_info())
print(c + c1)