# coding: utf-8
from math import hypot


class Vector(object):

    def __init__(self, x, y):
        super(object, self).__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y


if __name__ == "__main__":
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = Vector(3, 4)
    print(bool(Vector(0, 0)))

