# -*- coding: utf-8
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(45))
print(factorial.__doc__)
print(type(factorial))
fact = factorial

print(list(map(fact, range(11))))
print(dir(factorial))
print(factorial.__annotations__)
