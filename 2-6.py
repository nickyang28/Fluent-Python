# -*- coding:utf-8 -*-
import dis

t = (1, 2, [30, 40])
dis.dis('t[2] += [50, 60]')
try:
    t[2] += [50, 60]
except BaseException as err:
    print(err)
finally:
    print(t)
