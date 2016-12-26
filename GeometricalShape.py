'''
Define a class named Shape and its subclasses Square, Rectangle, Ellipse, Circle. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area of the shape where
Shape's area is 0 by default.
'''
from math import pi


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Ellipse(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return pi * self.a * self.b


class Circle(Ellipse):
    def __init__(self, r):
        Ellipse.__init__(self, r, r)

    def area(self):
        return Ellipse.area(self)


class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, s):
        Rectangle.__init__(self, s, s)

    def area(self):
        return Rectangle.area(self)


c = Circle(3)
r = Rectangle(3, 4)
s = Square(5)
e = Ellipse(9, 8)

print(e.area())
print(c.area())
print(r.area())
print(s.area())
