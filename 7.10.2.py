# -*- coding: utf-8 -*-
import time


def clock(fmt="[{elapsed: 0.8f}s] {name}({arg_str}) -> {result}"):
    def decorate(func):
        def clocked(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            name = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
            arg_str = ', '.join(arg_lst)
            print(fmt.format(**locals()))
            return result
        return clocked
    return decorate


@clock("[{elapsed: 0.8f}s] {name}({arg_str}) -> {result}")
def factorial(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
    return acc


if __name__ == '__main__':
    factorial(5)
