# -*- coding: utf-8 -*-
def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


if __name__ == '__main__':
    my_coro2 = simple_coro2(14)
    print(next(my_coro2))
    print(my_coro2.send(28))
    print(my_coro2.send(99))

