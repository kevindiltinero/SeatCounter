from src import create
from src import occupy
from src import count
from src import empty
from src import toggle



# This is creating the 2d array to represent the seating arrangement
# The count function is used directly after to test to see if all elements are there
seats = create.new_2d(5, 5)
counted_create = count.count_array(0, 5, 0, 5, seats)
print(seats)

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

