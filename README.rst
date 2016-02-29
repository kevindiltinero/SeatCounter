Seat Counter Program
====================

This is a software package which has been created to keep a running tally of occupied seats
within a two-dimensional square seating arrangement. The square contains 1000*1000 seats within it.

The basic program comprises 7 functions. Here is what each function these functions do:
CREATE: This function simply builds a two-dimensional array with two parameters to dictate the rows and columns amount
COUNT: counts how many empty chairs there are by iterating through every element in the array
OCCUPY:  changes a subset of the array to occupied based of 2 sets of coordinates.
TOGGLE: based on 2 sets of coordinates alternates empty to full and full to empty
EMPTY: uses coordinates to empty the seats in the selected subset
FILE: This function decodes the input file with line by line commands into executable instructions
EXECUTE: This takes the decoded instructions and executes the appropriate functons above based on the input feed.

MAIN FUNCTION
This ties it all together by creating the 2d array, feeding in the input file than sequentially going through line by line
and executing the functions above based on the input

TEST DRIVEN
This project was lead by test driven development. Every function that was created had a test built specifically for it
to check that the function was operating properly before moving onto the next one.