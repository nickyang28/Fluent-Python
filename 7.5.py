# -*- coding: utf-8 -*-
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, new_value):
        self._series.append(new_value)
        return self.average()

    def average(self):
        return sum(self._series) / len(self._series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager


def make_averager2():
    count = total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg2 = make_averager()
    print(avg2(10))
    print(avg2(11))
    print(avg2(12))
    print(avg2.__code__.co_varnames)
    print(avg2.__code__.co_freevars)

    avg3 = make_averager2()
    print(avg3(10))
    print(avg3(11))
    print(avg3(12))
    print(avg3.__code__.co_varnames)
    print(avg3.__code__.co_freevars)
