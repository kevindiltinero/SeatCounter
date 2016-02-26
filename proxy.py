from .context import sample

import unittest

working = [[0 for x in range(5)] for x in range(5)]


def occupy(a, b, c, d):
    for i in range(0, 5):
         for j in range(0, 5):
             working[i][j] = 1
    return working


def empty(a, b, c, d):
    for i in range(a, b):
         for j in range(c, d):
             working[i][j] = 0
    return working


def toggle(a, b, c, d):
    for i in range(a, b):
        for j in range(c, d):
            if (working[i][j] == 1):
                working[i][j] == 0
            elif (working[i][j] == 0):
                working[i][j] == 1
            else:
                pass
    return working


def counting():
    count = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if working[i][j] == 0:
                count += 1
    return count

print(working)
print(occupy(1, 5, 2, 5))
print(toggle(0, 5, 0, 5))
print(counting())
print(empty(0, 5, 0, 5))
print(counting())


