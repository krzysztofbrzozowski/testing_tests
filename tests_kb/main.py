"""
@author:    Krzysztof Brzozowski
@file:      main
@time:      27/11/2022
@desc:


Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> add(1, 2)
    3
    >>> multiply(2, 2)
    4
"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def devide(a, b):
    """
    >>> devide(10, 5)
    2.0
    """
    return a / b
