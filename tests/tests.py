from src import create
from src import count
from src import thefile
from src import occupy
from src import toggle
from src import empty

#THE TEST FOR THE CREATE FUNCTION
seats = create.new_2d(3, 3)
counted_create = count.count_array(3, 3, seats)


#TEST FOR OCCUPY
# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
seats = create.new_2d(3, 3)
occupied_seats = occupy.occupy_seats(0, 0, 1, 1, seats)
counted_occupy = count.count_array(3, 3, occupied_seats)

#TEST FOR EMPTY
# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
emptied_seats = empty.empty_it(0, 0, 2, 2, occupied_seats)
counted_emptied = count.count_array(3, 3, emptied_seats)

#TEST FOR TOGGLE
# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
seats = create.new_2d(3, 3)
counted_create = count.count_array(3, 3, seats)
toggled_seats = toggle.toggle_it(0, 0, 2, 2, occupied_seats)
counted_toggle = count.count_array(3, 3, toggled_seats)

#TEST THE FILE DECODE ()
check_commands = thefile.get_cmmds('inputfile.txt')