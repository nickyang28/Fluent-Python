# -*- coding: utf-8 -*-
from array import array
import math


class Vector:
    __slots__ = ('__x', "__y", "__angle")
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
        self.__angle = math.atan2(self.y, self.x)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def angle(self):
        return self.__angle

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(self)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle / math.pi)
            outer_fmt = '<{}, {}π>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y) ^ hash(abs(self))


if __name__ == "__main__":
    v1 = Vector(3, 4)
    print(v1.__slots__)
    print(v1.x, v1.y)
    x, y = v1
    print(v1)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(format(v1, '.3f'))
    print(hash(v1))
    v2 = Vector(1, 6)
    print({v1, v2})
    v3 = Vector.frombytes(bytes(v1))
    print(v3)
