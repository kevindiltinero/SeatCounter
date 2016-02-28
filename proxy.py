from .context import sample

import unittest

def create(a, b):
    working = [[0 for x in range(a)] for x in range(b)]
    return working

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


def toggle(a, b, c, d, nestedlist):
    for i in range(a, b):
        for j in range(c, d):
            if (nestedlist[i][j] == 1):
                nestedlist[i][j] == 0
            elif (nestedlist[i][j] == 0):
                nestedlist[i][j] == 1
            else:
                pass
    return nestedlist


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


# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
occupied_seats = occupy.occupy_seats(0, 3, 0, 3, seats)
counted_occupy = count.count_array(0, 5, 0, 5, seats)
print(occupied_seats)

# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
toggled_seats = toggle.toggle_it(0, 5, 0, 5, seats)
counted_toggle = count.count_array(0, 5, 0, 5, seats)
print(toggled_seats)

# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
emptied_seats = empty.empty_it(0, 5, 0, 5, occupied_seats)
counted_emptied = count.count_array(0, 5, 0, 5, emptied_seats)
print(emptied_seats)