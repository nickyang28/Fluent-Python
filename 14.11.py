# -*- coding: utf-8 -*-
from random import randint


def dice():
    yield randint(1, 6)


if __name__ == "__main__":
    print(next(dice()))
