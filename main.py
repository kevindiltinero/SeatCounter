from src import create
from src import occupy
from src import count

# This is creating the 2d array to represent the seating arrangement
# The count function is used directly after to test to see if all elements are there
seats = create.new_2d(5, 5)
counted_create = count.count_array(0, 5, 0, 5, seats)
print(seats)

# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
occupy_seats = occupy.occupy_seats(0, 3, 0, 3, seats)
counted_occupy = count.count_array(0, 5, 0, 5, seats)
print(occupy_seats)

counted_seats = count.count_array(0, 5, 0, 5, occupy_seats)
print(counted_seats)