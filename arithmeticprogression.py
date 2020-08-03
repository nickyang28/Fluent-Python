# -*- coding: utf-8 -*-
class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.end = end
        self.step = step

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 4)
    print(list(ap))
